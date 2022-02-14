from django.shortcuts import render, redirect
from .models import MySite, MyMember
from django.utils import timezone

def index(request):
    return render(request, 'index.html')