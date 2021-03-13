from django.db import models
from django.utils import timezone


class Classification(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Personality(models.Model):
    mbtitype = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
