from django.contrib import admin

# Register your models here.
from boats.models import Boat, Type

admin.site.register(Boat)
admin.site.register(Type)