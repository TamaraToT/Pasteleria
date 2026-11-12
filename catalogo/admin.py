from django.contrib import admin
from .models import Linea, Producto, Encargo


@admin.register(Linea)
class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'linea',
        'mostrar_precio',
        'porciones',
        'apto_celiacos',
        'stock',
        'disponible'
    )

    list_filter = ('linea', 'apto_celiacos', 'disponible')
    search_fields = ('nombre',)

    @admin.display(description='Precio')
    def mostrar_precio(self, obj):
        return f"${obj.precio:,}".replace(",", ".")


@admin.register(Encargo)
class EncargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'producto', 'nombre_cliente', 'cantidad', 'fecha_retiro')
    list_filter = ('producto', 'fecha_retiro')
    search_fields = ('nombre_cliente', 'correo')
