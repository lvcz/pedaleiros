from django.shortcuts import render, redirect
from .forms import CiclistasForm


def home(request):
    pass


def login(request):
    pass

def create(request):
    form = CiclistasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
