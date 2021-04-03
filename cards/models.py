from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Card(models.Model):
    term = models.TextField()
    definition = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
