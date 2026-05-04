from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'asunto', 'fecha']
    search_fields = ['nombre', 'email', 'asunto']
    readonly_fields = ['fecha']
