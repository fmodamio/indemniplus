# blog/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Entrada

def lista_entradas(request):
    entradas_list = Entrada.objects.all().order_by('-fecha_publicacion')
    paginator = Paginator(entradas_list, 5)  # Mostrar 5 entradas por página
    page_number = request.GET.get('page')  # Obtener el número de la página desde la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/lista_entradas.html', {'page_obj': page_obj})
