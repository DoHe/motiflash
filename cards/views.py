from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from cards.models import Card, Course


class Index(TemplateView):
    template_name = "index.html"


class Cards(TemplateView):
    template_name = "cards.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.request.GET.get("course")
        if course:
            context['cards'] = Card.objects.filter(course=course).all()
        return context


class Courses(TemplateView):
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class CardsX(View):

    def get(self, request):
        course = request.GET.get("course")
        cards = []
        if course:
            cards = cards_for_course(course)
        return JsonResponse({
            "cards": cards,
        })


def cards_for_course(course):
    cards = Card.objects.filter(course=course).all()
    return list(cards.values())
