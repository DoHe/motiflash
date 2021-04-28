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
