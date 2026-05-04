from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado correctamente! Te responderemos pronto.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor corregí los errores del formulario.')
    else:
        form = ContactoForm()

    return render(request, 'contacto/formulario.html', {'form': form})
