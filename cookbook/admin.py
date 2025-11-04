from django.contrib import admin
from cookbook.models import Recipe
# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass