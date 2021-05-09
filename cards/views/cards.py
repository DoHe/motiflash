from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.views.generic import FormView, TemplateView

from cards.forms import CardForm, CardFormSet
from cards.models import Card, Course


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


class CardEditView(LoginRequiredMixin, TemplateView):
    template_name = "cards_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(
            id=self.request.GET.get('course')
        )
        context['formset'] = CardFormSet(
            queryset=Card.objects.filter(course=context['course'])
        )
        return context

    def post(self, request):
        formset = CardFormSet(request.POST, request.FILES)
        if formset.is_valid():
            print(formset.save())
        return self.get(request)
