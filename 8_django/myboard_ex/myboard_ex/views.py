from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone



def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all().order_by('-id')})

def insert_form(request):
    return render(request, 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    if result:
        return redirect('index')

    else :
        return redirect('insertform')

def detail(request, id):
    return render(request, 'detail.html', {'dto' : MyBoard.objects.get(id=id)})