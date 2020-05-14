from django.contrib import admin
from unesco.models import Category, Iso, State, Region, Site
# Register your models here.

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Iso)
admin.site.register(Region)
admin.site.register(State)