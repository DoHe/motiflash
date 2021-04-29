# Generated by Django 3.2 on 2021-04-29 14:02

from django.db import migrations


def level_achievements(apps, schema_editor):
    LevelAchievement = apps.get_model('cards', 'LevelAchievement')
    l = LevelAchievement(
        title='First level up',
        description='You reached your very first new level!',
        level=2,
        icon='level_up'
    )
    l.save()
    for level in range(5, 105, 5):
        l = LevelAchievement(
            title=f'Reached level {level}',
            description=f"You reached level {level}!",
            level=level,
            icon='level_up'
        )
        l.save()


def reverse_level_achievements(apps, schema_editor):
    LevelAchievement = apps.get_model('cards', 'LevelAchievement')
    LevelAchievement.objects.filter(
        level__in=[2] + list(range(5, 105, 5))
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_levelachievement_siteachievement'),
    ]

    operations = [
        migrations.RunPython(
            level_achievements,
            reverse_level_achievements
        ),
    ]
