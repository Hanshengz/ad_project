from django.contrib import admin

# Register your models here.
from stars.models import Star, Type

admin.site.register(Star)
admin.site.register(Type)