
from django.shortcuts import render, get_object_or_404
from .models import Linea, Producto


def inicio(request):
    productos = Producto.objects.filter(disponible=True)
    lineas = Linea.objects.all()

    buscar = request.GET.get('buscar')
    linea_id = request.GET.get('linea')

    if buscar:
        productos = productos.filter(nombre__icontains=buscar)

    if linea_id:
        productos = productos.filter(linea_id=linea_id)

    return render(request, 'inicio.html', {
        'productos': productos,
        'lineas': lineas
    })


def detalle_producto(request, id):
    producto = get_object_or_404(
        Producto,
        id=id,
        disponible=True
    )

    return render(request, 'detalle.html', {
        'producto': producto
    })
