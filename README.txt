================================================================================
                    RECIPES BOOK - LIBRO DE RECETAS
================================================================================

Proyecto web de libro de recetas desarrollado con Django 5.2.7
Desplegado en producción en: https://recipes-book-mig7.onrender.com/

================================================================================
                                    CONTENIDO
================================================================================
1. DESCRIPCIÓN DEL PROYECTO
2. CARACTERÍSTICAS PRINCIPALES
3. TECNOLOGÍAS UTILIZADAS
4. ESTRUCTURA DEL PROYECTO
5. MODELO DE DATOS
6. INSTALACIÓN Y CONFIGURACIÓN
7. EJECUCIÓN LOCAL
8. DESPLIEGUE
9. FUNCIONALIDADES
10. INFORMACIÓN ADICIONAL

================================================================================
1. DESCRIPCIÓN DEL PROYECTO
================================================================================

Recipes Book es una aplicación web desarrollada en Django que permite a los usuarios
crear, visualizar y gestionar recetas de cocina. La aplicación está completamente
desplegada y funcionando en producción a través del servicio Render.

El proyecto utiliza una arquitectura Django estándar con un diseño moderno e
intuitivo, enfocado en una experiencia de usuario amigable y responsiva.

================================================================================
2. CARACTERÍSTICAS PRINCIPALES
================================================================================

📝 Gestión de Recetas
   - Crear nuevas recetas con información completa
   - Visualizar recetas en formato de tarjetas y vista detallada
   - Eliminar recetas existentes
   - Asociación automática con usuarios

🎨 Interfaz de Usuario
   - Diseño oscuro moderno y elegante
   - Totalmente responsivo (Bootstrap 5.3.2)
   - Navegación intuitiva con efectos hover
   - Tipografía personalizada (Nunito Sans)

⏱️ Información Detallada
   - Tiempo de preparación y cocción
   - Número de porciones
   - Ingredientes e instrucciones detalladas
   - Metadatos de creación y actualización

🔐 Gestión de Usuarios
   - Sistema de autenticación Django
   - Cada receta asociada a su autor
   - Interfaz en español (es-ar)

================================================================================
3. TECNOLOGÍAS UTILIZADAS
================================================================================

Backend:
- Django 5.2.7 - Framework web principal
- Python - Lenguaje de programación
- SQLite - Base de datos (desarrollo)
- PostgreSQL - Base de datos (producción)
- Gunicorn - Servidor WSGI para producción

Frontend:
- Bootstrap 5.3.2 - Framework CSS
- CSS3 personalizado con tema oscuro
- Nunito Sans - Tipografía principal

Herramientas de Producción:
- WhiteNoise - Servido de archivos estáticos
- dj-database-url - Configuración de base de datos
- python-dotenv - Gestión de variables de entorno
- psycopg2-binary - Adaptador PostgreSQL

Despliegue:
- Render - Plataforma de hosting
- Heroku-style Procfile para configuración

================================================================================
4. ESTRUCTURA DEL PROYECTO
================================================================================

recipes_book/
├── manage.py                           # Script de administración Django
├── Procfile                            # Configuración de despliegue
├── requirements.txt                    # Dependencias Python
├── db.sqlite3                         # Base de datos SQLite (desarrollo)
├── recipes_project/                    # Configuración principal Django
│   ├── settings.py                    # Configuración del proyecto
│   ├── urls.py                        # Enrutamiento de URLs
│   ├── wsgi.py                        # Aplicación WSGI
│   └── asgi.py                        # Aplicación ASGI
├── cookbook/                          # Aplicación principal de recetas
│   ├── models.py                      # Modelos de base de datos
│   ├── views.py                       # Vistas (lógica de la aplicación)
│   ├── forms.py                       # Formularios Django
│   ├── admin.py                       # Configuración del admin
│   ├── static/cookbook/               # Archivos estáticos
│   │   ├── style.css                  # Estilos CSS personalizados
│   │   └── fonts/                     # Archivos de fuentes
│   └── templates/cookbook/            # Plantillas HTML
│       ├── base.html                  # Plantilla base
│       ├── recipes_grid.html          # Vista de cuadrícula
│       ├── recipes_card.html          # Tarjeta de receta
│       ├── recipe_detail.html         # Detalle de receta
│       ├── recipe_form.html          # Formulario de receta
│       └── recipe_confirm_delete.html # Confirmación de eliminación
└── .venv/                             # Entorno virtual

================================================================================
5. MODELO DE DATOS
================================================================================

Modelo Recipe:
- title: CharField (max_length=200) - Título de la receta
- description: TextField - Descripción general
- ingredients: TextField - Lista de ingredientes
- instructions: TextField - Instrucciones paso a paso
- preparation_time: PositiveIntegerField - Tiempo de preparación (minutos)
- cooking_time: PositiveIntegerField - Tiempo de cocción (minutos)
- servings: PositiveIntegerField - Número de porciones
- created_at: DateTimeField - Fecha de creación (automático)
- updated_at: DateTimeField - Fecha de actualización (automático)
- author: ForeignKey(User) - Autor de la receta

Características del modelo:
- Nombres en español (verbose_name)
- Ordenamiento por fecha de creación (más reciente primero)
- URL absoluta configurada para vistas
- Relación con modelo User de Django

================================================================================
6. INSTALACIÓN Y CONFIGURACIÓN
================================================================================

Requisitos previos:
- Python 3.8+ instalado
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar)

Pasos de instalación:

1. Clonar el repositorio:
   git clone [URL_DEL_REPOSITORIO]
   cd recipes_book

2. Crear y activar entorno virtual:
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Configurar variables de entorno (opcional para desarrollo):
   SECRET_KEY=tu_clave_secreta_aqui
   DATABASE_URL=sqlite:///db.sqlite3

5. Ejecutar migraciones de la base de datos:
   python manage.py makemigrations
   python manage.py migrate

6. Crear superusuario (opcional, para panel de admin):
   python manage.py createsuperuser

================================================================================
7. EJECUCIÓN LOCAL
================================================================================

Iniciar el servidor de desarrollo:
   python manage.py runserver

La aplicación estará disponible en: http://127.0.0.1:8000/

Comandos útiles:
- python manage.py runserver - Iniciar servidor desarrollo
- python manage.py makemigrations - Crear migraciones
- python manage.py migrate - Aplicar migraciones
- python manage.py collectstatic - Recolectar archivos estáticos
- python manage.py createsuperuser - Crear administrador

================================================================================
8. DESPLIEGUE
================================================================================

El proyecto está configurado para despliegue en producción:

Configuración de producción:
- Base de datos PostgreSQL (configurada por RENDER_DATABASE_URL)
- Archivos estáticos servidos con WhiteNoise
- Gunicorn como servidor WSGI
- DEBUG=False en producción
- CSRF_TRUSTED_ORIGINS configurado para Render

Variables de entorno requeridas en producción:
- SECRET_KEY: Clave secreta de Django
- DATABASE_URL: URL de conexión a base de datos
- ALLOWED_HOSTS: Hosts permitidos

El archivo Procfile configura:
   web: gunicorn recipes_project.wsgi:application --bind 0.0.0.0:$PORT --preload

================================================================================
9. FUNCIONALIDADES
================================================================================

Vistas implementadas:
1. Base View (create) - Página principal con lista de recetas
2. RecipeCreateView - Creación de nuevas recetas
3. RecipeDetailView - Vista detallada de recetas
4. RecipeDeleteView - Eliminación de recetas

URLs configuradas:
- / - Página principal con todas las recetas
- /recipe/<pk>/ - Detalle de receta específica
- /recipe/new/ - Formulario para crear nueva receta
- /recipe/<pk>/delete/ - Confirmación y eliminación de receta

Funcionalidades del usuario:
- Ver todas las recetas en formato de cuadrícula
- Acceder al detalle de cualquier receta
- Crear nuevas recetas con formulario validado
- Eliminar recetas existentes
- Navegación intuitiva entre páginas

================================================================================
10. INFORMACIÓN ADICIONAL
================================================================================

Configuración Regional:
- Idioma: español (es-ar)
- Zona horaria: America/Buenos_Aires
- Formato de fecha y hora local

Seguridad:
- CSRF protection habilitado
- Secure cookies en producción
- SSL redirect configurado para producción
- Secret key gestionada por variables de entorno

Personalización:
- Tema oscuro personalizado
- Fuentes Nunito Sans
- Animaciones y transiciones CSS
- Diseño responsivo para móviles

Extensibilidad:
El proyecto está estructurado para facilitar la adición de:
- Sistema de calificación de recetas
- Búsqueda y filtrado avanzado
- Categorías y etiquetas
- Imágenes de recetas
- Comentarios y reseñas
- Compartir en redes sociales

================================================================================
                           INFORMACIÓN DE CONTACTO
================================================================================

Proyecto desarrollado como parte del curso de Diseño Web
Desplegado en: https://recipes-book-mig7.onrender.com/

Para consultas técnicas o preguntas sobre el proyecto,
referirse a la documentación de Django 5.2.7 disponible en:
https://docs.djangoproject.com/en/5.2/

================================================================================
                                FIN DEL DOCUMENTO
================================================================================