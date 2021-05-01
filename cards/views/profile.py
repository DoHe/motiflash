from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View

from cards.models import LevelAchievement, Profile, SiteAchievement

POINTS = {
    'card_correct': 1,
    'course_finished': 10,
    'course_mostly_correct': 20,
    'course_perfect': 30,
}

LEVELS = [
    (0, 1),
    (100, 2),
    (200, 3)
]


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
    success_url = reverse_lazy('profile')
    template_name = 'registration/signup.html'


class PointsView(LoginRequiredMixin, View):

    def get(self, request):
        reason = request.GET.get('reason')
        points = POINTS.get(reason)

        response = {"status": "ok", "points": points}
        if points:
            new_points = request.user.profile.experience_points + points
            print(new_points)
            request.user.profile.experience_points = new_points
            level = 0
            for idx, (needed_points, level) in enumerate(LEVELS):  # TODO: Fix logic
                if needed_points > new_points:
                    level = LEVELS[idx-1][1]
            request.user.profile.level = level
            request.user.profile.save()

        else:
            response["status"] = "error"

        return JsonResponse(response)


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
