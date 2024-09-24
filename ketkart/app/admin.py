from django.contrib import admin

# Register your models here.
from .models import category, sub_category

admin.site.register(category)

admin.site.register(sub_category)