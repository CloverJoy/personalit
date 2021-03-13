from django.db import models


class Classification(models.Model):
    name = models.CharField(max_length=255)


class Personality(models.Model):
    mbtitype = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    classification = models.ForeignKey(
        Classification, on_delete=models.CASCADE)
