from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # Configuración extendida para cambiar el nombre de la aplicación en el sector admin
    verbose_name = 'Blog' 