from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Recipe, RecipeAdmin)

# Register your models here.
