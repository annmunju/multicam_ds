from django.shortcuts import render

def index(request):
    return render(request, "index.html", {'name' : 'munju'}) # {변수명 : 값}을 여기에 넣어줌!