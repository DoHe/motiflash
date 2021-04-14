from django import forms

from cards.models import Course, Card
from cards.utils import parse_export


class CourseForm(forms.ModelForm):
    import_text = forms.CharField(
        widget=forms.Textarea,
        required=False
    )

    class Meta:
        model = Course
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if Course.objects.filter(name=name).exists():
            raise forms.ValidationError("Course name already exists")
        return name

    def clean_import_text(self):
        import_text = self.cleaned_data['import_text']
        if not import_text:
            return ""

        try:
            parsed = parse_export(import_text)
        except:
            raise forms.ValidationError(
                "Import text not valid (tab and newline separate expected)"
            )

        valid = len(parsed) > 0 and all(len(i) == 2 for i in parsed)
        if not valid:
            raise forms.ValidationError(
                "Import text not valid (list of tuples expected)"
            )

        return parsed


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'
