from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from cards.models import Card, Course, Notifications, LevelAchievement, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Card)
admin.site.register(Course)
admin.site.register(Notifications)
admin.site.register(LevelAchievement)
admin.site.register(Profile)
