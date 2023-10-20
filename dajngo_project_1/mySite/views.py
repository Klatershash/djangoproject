from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def blog(request):
    return render(request, 'blog.html')


def reg(request):
    return render(request, 'reg.html')


def auth(request):
    return render(request, 'auth.html')