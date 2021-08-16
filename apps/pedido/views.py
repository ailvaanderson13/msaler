from django.shortcuts import render
from . import forms, models
from apps.cliente.models import Cliente
from apps.item.models import Item


def create_pedido(request):
    page_title = 'Novo Pedido'
    notification = None
    msg = None
    loja = request.user.loja
    employee = request.user

    clientes = Cliente.objects.filter(is_active=True)

    produtos = Item.objects.filter(is_active=True)

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'clientes': clientes, 'produtos': produtos
    }

    return render(request, 'cadastro_pedido.html', context)


def list_pedidos(request):
    page_title = 'Pedidos Cadastrados'
    msg = None
    notification = None

    pedidos = models.Pedido.objects.filter(is_active=True)

    if not pedidos:
        msg = 'Nenhum Pedido Cadastrado!'
        notification = 'danger'

    context = {
        'page_title': page_title, 'pedidos': pedidos, 'msg': msg, 'notification': notification
    }
    return render(request, 'pedidos_cadastrados.html', context)