from django.apps import AppConfig
from django.contrib.auth.models import User


if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'correo@gmail.com', '12345678')


class ContactoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacto'

