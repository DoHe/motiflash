from django import forms
from cards.models import Course, Card


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if Course.objects.filter(name=name).exists():
            raise forms.ValidationError("Course name already exists")
        return name


class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = '__all__'
