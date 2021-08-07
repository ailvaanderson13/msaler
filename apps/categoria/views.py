from django.shortcuts import render
from . import forms, models


def new_category(request, pk=None):
    page_title = "Cadastro de Categoria" if not pk else "Editar Categoria"
    form = forms.CategoriaForm()
    msg = None
    notification = None
    categoria = None
    loja = request.user.loja

    if pk:
        categoria = models.Category.objects.get(pk=pk)

        if categoria:
            form = forms.CategoriaForm(instance=categoria)

    if request.method == 'POST':
        if categoria:
            form = forms.CategoriaForm(request.POST, instance=categoria)
        else:
            form = forms.CategoriaForm(request.POST)

        try:
            if form.is_valid():
                if categoria:
                    form.save()
                    msg = 'Editado com Sucesso!'
                    notification = 'success'
                else:
                    new_categoria = form.save(commit=False)
                    new_categoria.loja = loja
                    new_categoria.save()
                    msg = 'Salvo com Sucesso!'
                    notification = 'success'
                form = forms.CategoriaForm()
            else:
                msg = 'erro ao salvar'
                notification = 'danger'
        except Exception as e:
            print(e)
    context = {
        'page_title': page_title, 'notification': notification, 'msg': msg, 'form': form
    }
    return render(request, 'cadastro_categoria.html', context)


def list_categoria(request):
    page_title = 'Categorias Cadastradas'
    categorias = None
    msg = None
    notification = None
    loja = request.user.loja

    categorias = models.Category.objects.filter(is_active=True)

    if not categorias:
        msg = 'Nenhuma Categoria cadastradas'
        notification = 'danger'

    context = {
        'page_title': page_title, 'categorias': categorias, 'msg': msg, 'notification': notification
    }

    return render(request, 'categorias_cadastradas.html', context)

