from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # access = models.ManyToManyField(User)


class Card(models.Model):
    term = models.TextField()
    definition = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
