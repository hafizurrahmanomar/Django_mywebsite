from django.shortcuts import redirect, render
from . forms import *

# Create your views here.


def home(request):
    context = {}
    return render(request, 'myapp/home.html', context)


def about(request):
    return render(request, 'myapp/about.html')


def CreateMobile(request):
    form = CreateUpdateMobile()
    if request.method == "POST":
        form = CreateUpdateMobile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'myapp/mobile_form.html', context)
