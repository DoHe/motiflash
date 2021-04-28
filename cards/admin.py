from django.contrib import admin

from cards.models import Card, Course, Notifications

admin.site.register(Card)
admin.site.register(Course)
admin.site.register(Notifications)
