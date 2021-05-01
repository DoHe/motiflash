from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owning_user'
    )
    access = models.ManyToManyField(
        User,
        related_name='allowed_user'
    )


class Card(models.Model):
    term = models.TextField()
    definition = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    achieved = models.ManyToManyField(
        User,
        related_name='achieving_user'
    )


class SiteAchievement(Achievement):
    path = models.CharField(max_length=100)


class LevelAchievement(Achievement):
    level = models.IntegerField(null=False)

    def save(self, *args, **kwargs):
        if not self.icon:
            self.icon = 'level_up'
        if not self.description:
            self.description = f"You reached level {self.level}!"
        if not self.title:
            self.title = f'Reached level {self.level}'
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
