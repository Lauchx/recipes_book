
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from cookbook.forms import RecipeForm
from cookbook.models import Recipe

# Create your views here.
def create(request):
    recipes_list = Recipe.objects.all()
    print(recipes_list)
    return render(request, 'cookbook/base.html', context = {'recipes': recipes_list} )


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm 
    success_url = reverse_lazy('base') 

class RecipeDetailView(DetailView):
    model = Recipe 
    context_object_name = "recipe" 
    

