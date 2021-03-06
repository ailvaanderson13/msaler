from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect


def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('utils:login')

    page_title = 'DASHBOARD'

    context = {
        'page_title': page_title
    }
    return render(request, 'dashboard/dashboard.html', context)


def acesso(request):
    if request.user.is_authenticated:
        return redirect('utils:dashboard')

    erro = False
    msg = None

    if request.method == 'POST':
        email = request.POST.get('email', None)
        senha = request.POST.get('password', None)
        user = authenticate(username=email, password=senha)

        if user:
            login(request, user)
            return redirect('utils:dashboard')
        else:
            erro = True
            msg = 'Usuário ou senha inválidos!'

    context = {
        'erro': erro, 'msg': msg
    }
    return render(request, 'login/login.html', context)


def logout_(request):
    return logout_then_login(request, login_url='/login')