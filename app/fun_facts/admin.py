from django.contrib import admin
from .models import DatesFact, PopularDates

# Register your models here.

admin.site.register([DatesFact, PopularDates])
