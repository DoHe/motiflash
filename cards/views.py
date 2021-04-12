from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect

from cards.models import Card, Course
from cards.forms import CourseForm, CardForm


class Index(TemplateView):
    template_name = "index.html"


class Cards(TemplateView):
    template_name = "cards.html"

    def get(self, request):
        self.course = self.request.GET.get("course")
        if not self.course:
            return redirect('courses')
        self.cards = list(
            Card.objects.filter(course=self.course).all().values()
        )
        if not self.cards:
            return redirect('cards_add')

        return super().get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.course:
            context['cards'] = self.cards
            context['course'] = Course.objects.get(id=self.course)
        return context


class CardAddView(FormView):
    template_name = "card_add.html"
    form_class = CardForm
    success_url = "."

    def form_valid(self, form):
        card = Card(**form.cleaned_data)
        card.save()
        return super().form_valid(form)


class Courses(FormView):
    template_name = "courses.html"
    form_class = CourseForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

    def form_valid(self, form):
        course = Course(**form.cleaned_data)
        course.save()
        return super().form_valid(form)
