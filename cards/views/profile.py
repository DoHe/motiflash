from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from cards.models import LevelAchievement, SiteAchievement


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class AchievementsView(LoginRequiredMixin, TemplateView):
    template_name = "achievements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['level_achievements'] = LevelAchievement.objects.all()
        context['site_achievements'] = SiteAchievement.objects.all()
        return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
