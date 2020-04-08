
# Register your models here.

from django.contrib import admin
from .models import Lawnmower, Fertilizer

admin.site.register(Lawnmower)
admin.site.register(Fertilizer)