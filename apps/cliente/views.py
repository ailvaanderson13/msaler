from django.shortcuts import render
from . import models, forms


def cadastro_update_cliente(request, pk=None):
    page_title = 'Cadastro de Cliente' if not pk else 'Editar Cliente'
    msg = None
    notification = None
    cliente = None
    form = forms.FormCliente()
    loja = request.user.loja

    if pk:
        cliente = models.Cliente.objects.get(pk=pk)
        if cliente:
            form = forms.FormCliente(instance=cliente)
        else:
            msg = 'Nenhum cliente encontrado!'
            notification = 'danger'

    if request.method == 'POST':
        if cliente:
            form = forms.FormCliente(request.POST, instance=cliente)
        else:
            form = forms.FormCliente(request.POST)

        if form.is_valid():
            if cliente:
                form.save()
                msg = 'Cliente editado(a) com Sucesso!'
                notification = 'success'
            else:
                new_cliente = form.save(commit=False)
                new_cliente.loja = loja if loja else None
                new_cliente.save()
                msg = 'Cliente Cadastrado(a) com Sucesso!'
                notification = 'success'
            form = forms.FormCliente()
        else:
            if 'cpf' in form.errors:
                msg = f'CPF digitado já possui cadastro'
                notification = 'warning'

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }

    return render(request, 'cadastro_cliente.html', context)


def list_cliente(request):
    page_title = 'Clientes Cadastrados(as)'
    msg = None
    notification = None
    clientes = None

    clientes = models.Cliente.objects.filter(is_active=True)

    if not clientes:
        msg = 'Nenhum cliente Cadastrado(a)'
        notification = 'danger'

    context = {
        'clientes': clientes, 'notification': notification, 'msg': msg, 'page_title': page_title
    }

    return render(request, 'clientes_cadastrados.html', context)