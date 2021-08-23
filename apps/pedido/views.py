from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import forms, models
from apps.cliente.models import Cliente
from apps.item.models import Item
from apps.utils.function_aux.random import str_generator
import json


@csrf_exempt
def safe_pedido(request):
    response = {
        'success': False
    }
    list_pedido = None
    pk_cliente = None
    forma_pag = None
    obs = None
    funcionario = request.user
    loja = request.user.loja

    if request.method == 'POST':
        list_pedido = json.loads(request.POST['list_pedido'])
        pk_cliente = request.POST.get('id_cliente', None)
        forma_pag = request.POST.get('forma_pag', None)
        obs = request.POST.get('obs', None)

    if list_pedido and pk_cliente:
        pk_cliente = int(pk_cliente)
        cod = str_generator()
        equals = models.Pedido.objects.filter(codigo=cod)
        while equals:
            cod = str_generator()

        new_pedido = models.Pedido.objects.create(codigo=cod, employee=funcionario, cliente_id=pk_cliente, loja=loja,
                                                  forma_pag=forma_pag, obs=obs, detalhes=list_pedido)

        for l in list_pedido:
            if type(l) == dict:
                for k, v in l.items():
                    for i in v:
                        for x in i['id-produto']:
                            new_pedido.item.add(int(x))

        new_pedido.save()

        response['success'] = True

    return JsonResponse(response, safe=False)


def create_pedido(request):
    page_title = 'Novo Pedido'
    notification = None
    msg = None
    loja = request.user.loja
    employee = request.user

    clientes = Cliente.objects.filter(is_active=True)

    produtos = Item.objects.filter(is_active=True).order_by('nome')

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