import math

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
    'course_perfect': 20,
}

LEVEL_EXPONENT = 1.4
LEVEL_BASE = 100


def generate_levels(level):
    return math.floor(LEVEL_BASE * (level ** LEVEL_EXPONENT))


LEVEL_BREAK_POINTS = [
    generate_levels(i)
    for i in range(100)
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


def level_for_points(points):
    for idx in range(len(LEVEL_BREAK_POINTS)):
        next_idx = idx + 1
        if next_idx == len(LEVEL_BREAK_POINTS):
            return next_idx

        next_points = LEVEL_BREAK_POINTS[next_idx]
        if points < next_points:
            return next_idx
    return -1


class PointsView(LoginRequiredMixin, View):

    def get(self, request):
        reason = request.GET.get('reason')
        points = POINTS.get(reason)

        response = {"status": "ok", "points": points}
        if points:
            new_points = request.user.profile.experience_points + points
            request.user.profile.experience_points = new_points
            new_level = level_for_points(new_points)
            request.user.profile.level = new_level
            request.user.profile.save()
            for achievement in LevelAchievement.objects.all():
                if new_level == achievement.level:
                    achievement.achieved.add(request.user)
                    achievement.save()
        else:
            response["status"] = "error"

        return JsonResponse(response)


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
