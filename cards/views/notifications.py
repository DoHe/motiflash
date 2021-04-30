from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from cards.models import Notifications


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
