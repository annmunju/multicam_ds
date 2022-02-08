from django.shortcuts import render, redirect
from .models import MyBoard, MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password


def index(request):
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard, 5)
    page_num = request.GET.get('page', '1')

    # 페이지에 맞는 모델 가져오기
    page_obj = paginator.get_page(page_num)

    # 관련 메서드
    print(page_obj) # <Page 11 of 22>
    print(type(page_obj)) # <class 'django.core.paginator.Page'>
    print(page_obj.count) # <bound method Sequence.count of <Page 11 of 22>>
    print(page_obj.paginator.num_pages) # 22
    print(page_obj.paginator.page_range) # range(1, 23)
    print(page_obj.has_next()) # True
    print(page_obj.has_previous()) # True
    try:
        print(page_obj.next_page_number()) # 12
        print(page_obj.previous_page_number()) # 10
    except:
        pass
    print(page_obj.start_index()) # 51
    print(page_obj.end_index()) # 55

    return render(request, 'index.html', {'list': page_obj})


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    else:
        myname = request.POST['myname']
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

        if result:
            return redirect('index')
        else:
            return redirect('insertform')


def update(request, id):
    if request.method == 'GET':
        return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})
    else:
        mytitle = request.POST['mytitle']
        mycontent = request.POST['mycontent']

        myboard = MyBoard.objects.filter(id=id)
        result_title = myboard.update(mytitle=mytitle)
        result_content = myboard.update(mycontent=mycontent)

        if result_title + result_content == 2:
            return redirect(f'/detail/{id}')
        else:
            return redirect(f'/updateform/{id}')


def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect(f'/detail/{id}')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        mymember = MyMember(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save()

        return redirect('/')