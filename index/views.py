from django.shortcuts import render, redirect
from .forms import DatosFormularioForm
from .models import DatosFormulario

def get_ip(request):
    # Intenta obtener la IP desde el encabezado HTTP_X_FORWARDED_FOR (útil si estás detrás de un proxy)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # Si no hay proxy, obtener la IP directamente desde REMOTE_ADDR
        ip = request.META.get('REMOTE_ADDR')
    return ip

def enviar_formulario(request):
    if request.method == 'POST':
        form = DatosFormularioForm(request.POST)
        if form.is_valid():
            ip_address = get_ip(request)
            DatosFormulario.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                telefono=form.cleaned_data['telefono'],
                mensaje=form.cleaned_data['mensaje'],
                ip_address=ip_address
            )
            return redirect('index_gracias')  # Redirige a una página de agradecimiento
    else:
        form = DatosFormularioForm()
    
    return render(request, 'index/index.html', {'form': form})

def gracias(request):
    return render(request, 'index/gracias.html')

def legal(request):
    return render(request, 'index/legal.html')
    
def medica(request):
    return render(request, 'index/medica.html')
