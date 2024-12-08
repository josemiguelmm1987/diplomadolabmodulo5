from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock', 'categoria', 'disponible')
    ordering = ('nombre',)
    search_fields = ('nombre', )
    list_filter = ('disponible', )
admin.site.register(Producto,ProductoAdmin)