from django.contrib import admin

# Register your models here.
from MercadoAgro.Apps.MercadoagroFinal.models import *

admin.site.register(usuario)
admin.site.register(producto)
admin.site.register(compra)