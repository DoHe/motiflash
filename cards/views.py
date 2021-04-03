from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from cards.models import Card


class Index(TemplateView):
    template_name = "index.html"


class Cards(View):

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
