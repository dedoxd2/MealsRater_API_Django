from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# Search for those topics
# uuid , slugify


class Meal (models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    def avg_rating(self):
        # sum of ratings stars / len of rating how many ratings
        sum = 0
        ratings = ratings = Rating.objects.filter(meal=self)
        number = 0
        for rate in ratings:
            sum += rate.stars
            number += 1

        if number > 0:
            avg = float(sum) / float(number)
            return avg
        else:
            return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.meal.title

    class Meta:
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)
