from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView

from cards.forms import CardForm, CourseForm, ShareForm
from cards.models import Card, Course, Notifications, LevelAchievement, SiteAchievement


class Index(TemplateView):
    template_name = "index.html"


class AchievementsView(LoginRequiredMixin, TemplateView):
    template_name = "achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['level_achievements'] = LevelAchievement.objects.all()
        context['site_achievements'] = SiteAchievement.objects.all()
        return context


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
        user_has_access = (
            Q(owner=self.request.user) |
            Q(access=self.request.user)
        )
        context['courses'] = Course.objects.filter(user_has_access)
        return context

    def form_valid(self, form):
        import_text = form.cleaned_data.pop("import_text")
        form.cleaned_data["owner"] = self.request.user
        course = Course(**form.cleaned_data)
        course.save()
        if import_text:
            for (term, definition) in import_text:
                card = Card(term=term, definition=definition, course=course)
                card.save()
        return super().form_valid(form)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ShareView(LoginRequiredMixin, FormView):
    template_name = "share.html"
    form_class = ShareForm
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        course = Course.objects.get(
            id=self.request.GET.get('course')
        )
        for user_id in form.cleaned_data.get("user", []):
            user = User.objects.get(
                id=user_id
            )
            course.access.add(user)
        course.save()
        return super().form_valid(form)


class NotificationsView(LoginRequiredMixin, View):

    def get(self, request):
        notifications = Notifications.objects.filter(receiver=request.user)
        return JsonResponse(
            list(notifications.values()),
            safe=False
        )


class NotificationReadView(LoginRequiredMixin, View):

    def get(self, request):
        status = "ok"
        try:
            notification_id = request.GET.get('id')
            Notifications.objects.get(id=notification_id).delete()
        except:
            status = "failed"
        return JsonResponse({
            "status": status
        })
