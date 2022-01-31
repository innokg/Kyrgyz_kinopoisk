from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    review = models.TextField()
    scores = models.PositiveIntegerField
    stuff_id = models.ForeignKey

class Genres(models.Model):
    slug = models.ForeignKey
    names = models.CharField(max_length=100)

class Stuff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    biography = models.TextField()

class Favourites(models.Model):
    movie_id = models.ForeignKey
    user_id = models.ForeignKey



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    age = models.PositiveIntegerField()

