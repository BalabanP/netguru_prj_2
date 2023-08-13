from django.db import models

# Create your models here.


class DatesFact(models.Model):
    month = models.IntegerField()
    day = models.IntegerField()
    fact = models.TextField(max_length=200)

    class Meta:
        unique_together = ("month", "day")


class PopularDates(models.Model):
    month = models.CharField(max_length=20)
    days_checked = models.IntegerField()
