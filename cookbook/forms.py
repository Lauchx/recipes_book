from django import forms

from cookbook.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions','preparation_time', 'cooking_time', 'servings', 'author']