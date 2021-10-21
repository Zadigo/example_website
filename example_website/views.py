from django.shortcuts import render


def view(request, *args, **kwargs):
    return render(request, 'index.html', {})
