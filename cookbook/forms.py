from django import forms

from cookbook.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions','preparation_time', 'cooking_time', 'servings', 'author']
        widgets = {}

    def __init__(self, *args, **kwargs):
        # Llamamos al constructor original del ModelForm
        super().__init__(*args, **kwargs)
        
        # Iteramos sobre todos los campos visibles en el formulario
        for field_name, field in self.fields.items():
            
            # 1. Aplicamos las clases CSS de Bootstrap (form-control y colores)
            # Nota: text-light se añade para asegurar el contraste sobre bg-dark
            field.widget.attrs['class'] = 'form-control bg-secondary border-0'

            # 2. Lógica opcional para añadir un placeholder solo a campos de texto
            field.widget.attrs['placeholder'] = f'Ingrese el {field_name} de la receta'
            
            # 3. Lógica para campos de tipo Textarea (si Recipe tiene un campo como 'contenido')
            # Es importante asegurarse de que el fondo y texto también se apliquen al widget correcto
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 5
                # Las clases ya están aplicadas arriba