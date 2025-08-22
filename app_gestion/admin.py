from django.contrib import admin
from .models import Contacto, Obituario, DetalleObituario, Blog


# Register your models here.
admin.site.register(Contacto)  # Contacto is defined in models.py   
admin.site.register(Blog)  # Blog is defined in models.py   

#admin.site.register(Obituario)  # Obituario is also defined in models.py

class DetalleObituarioInline(admin.StackedInline):
    model = DetalleObituario
    can_delete = False
    max_num = 1  # Solo un detalle por obituario

class ObituarioAdmin(admin.ModelAdmin):
    inlines = [DetalleObituarioInline]

admin.site.register(Obituario, ObituarioAdmin)
