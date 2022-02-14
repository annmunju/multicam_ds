from django.shortcuts import render, redirect
from django.utils import timezone


def index(request):
    return render(request, 'index.html')