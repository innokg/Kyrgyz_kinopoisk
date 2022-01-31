from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    review = models.TextField()
    scores = models.PositiveIntegerField
    stuff_id = models.ForeignKey

