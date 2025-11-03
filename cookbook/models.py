from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    """
    Modelo que representa una receta de cocina.
    Cada receta está asociada a un usuario (autor).
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    ingredients = models.TextField(help_text="Ingresa los ingredientes, uno por línea o separados por comas",
                                  verbose_name="Ingredientes")
    instructions = models.TextField(help_text="Describe paso a paso cómo preparar la receta",
                                   verbose_name="Instrucciones")
    preparation_time = models.PositiveIntegerField(help_text="Tiempo en minutos",
                                                 default=30, verbose_name="Tiempo de preparación")
    cooking_time = models.PositiveIntegerField(help_text="Tiempo en minutos",
                                              default=0, verbose_name="Tiempo de cocción")
    servings = models.PositiveIntegerField(default=4, verbose_name="Porciones")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")

    class Meta:
        verbose_name = "recipe"
        verbose_name_plural = "recipes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Devuelve la URL absoluta para una instancia específica de Recipe.
        Django usa este método en vistas CreateView, UpdateView, DeleteView.
        """
        return reverse('recipe-detail', kwargs={'pk': self.pk})
