from django.shortcuts import render
from . import models, forms


def create_update_item(request, pk=None):
    page_title = 'Cadastro de produto' if not pk else 'Editar Produto'
    msg = None
    notification = None
    form = forms.ItemForm()
    item = None
    loja = request.user.loja

    if pk:
        item = models.Item.objects.get(pk=pk, is_active=True)
        if item:
            form = forms.ItemForm(instance=item)
        else:
            msg = 'Nenhum Produto Encontrado'
            notification = 'danger'

    if request.method == 'POST':
        if item:
            form = forms.ItemForm(request.POST, instance=item)
        else:
            form = forms.ItemForm(request.POST)

        if form.is_valid():
            if item:
                form.save()
                msg = 'Produto Atualizado com Sucesso!'
                notification = 'success'
            else:
                new_item = form.save(commit=False)
                new_item.loja = loja if loja else None
                new_item.save()
                msg = 'Produto Cadastrado com Sucesso!'
                notification = 'success'
            form = forms.ItemForm()
        else:
            msg = form.errors
            notification = 'danger'

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }

    return render(request, 'cadastro_item.html', context)


def list_item(request):
    page_title = 'Produtos Cadastrados'
    msg = None
    notification = None
    itens = None

    itens = models.Item.objects.filter(is_active=True)

    if not itens:
        msg = "Nenhum Produto Cadastrado"
        notification = 'danger'

    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'itens': itens
    }

    return render(request, 'itens_cadastrados.html', context)