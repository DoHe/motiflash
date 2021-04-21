from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from cards.models import Card, Course
from cards.forms import CourseForm, CardForm


class Index(TemplateView):
    template_name = "index.html"


class Cards(LoginRequiredMixin, TemplateView):
    template_name = "cards.html"

    def get(self, request):
        self.course = self.request.GET.get("course")
        if not self.course:
            return redirect('courses')
        self.cards = list(
            Card.objects.filter(course=self.course).all().values()
        )
        if not self.cards:
            return redirect(f"{reverse('cards_add')}?course={self.course}")

        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.course:
            context['cards'] = self.cards
            context['course'] = Course.objects.get(id=self.course)
        return context


class CardAddView(LoginRequiredMixin, FormView):
    template_name = "card_add.html"
    form_class = CardForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(
            id=self.request.GET.get('course')
        )
        return context

    def form_valid(self, form):
        card = Card(**form.cleaned_data)
        card.save()
        return super().form_valid(form)

    def get_success_url(self):
        params = self.request.GET.copy()
        form = self.get_form()
        params['success'] = form['term'].value()
        return f'.?{params.urlencode()}'


class Courses(LoginRequiredMixin, FormView):
    template_name = "courses.html"
    form_class = CourseForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

    def form_valid(self, form):
        import_text = form.cleaned_data.pop("import_text")
        course = Course(**form.cleaned_data)
        course.save()
        if import_text:
            for (term, definition) in import_text:
                card = Card(term=term, definition=definition, course=course)
                card.save()
        return super().form_valid(form)
