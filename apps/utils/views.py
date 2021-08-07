from django.shortcuts import render


def dashboard(request):
    page_title = 'DASHBOARD'

    context = {
        'page_title': page_title
    }
    return render(request, 'dashboard/dashboard.html', context)
