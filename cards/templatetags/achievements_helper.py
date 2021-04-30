from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def achievement_icon(achievement, user):
    achieved = achievement_achieved(achievement, user)
    status = 'active' if achieved else 'inactive'
    return static(f'cards/icons/{achievement.icon}_{status}.svg')


@register.simple_tag
def achievement_achieved(achievement, user):
    return achievement.achieved.filter(id=user.id).exists()
