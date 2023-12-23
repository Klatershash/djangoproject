from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, User, Category, Friend, Chat
from  .forms import AddArticle
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def blog(request):
    articles = Article.objects.all()
    articles_new = []
    for article in articles:
        articles_new.append({
            'title':article.title,
            'image':str(article.image).split('/')[-1],
            'description':article.description,
            'id':article.id,
            'cat':article.category.title,
            'user':article.user.login
        })
    #print(articles_new)
    a = {
        'articles':articles_new
    }
    return render(request, 'blog.html', context=a)


def reg(request):
    suc = ''
    error = ''
    if request.method == 'POST':
        if User.objects.filter(login=request.POST['login']).exists():
            error += 'Пользователь с логином '+request.POST['login']+' же существует'
        else:
            user = User()
            user.login = request.POST['login']
            user.password = request.POST['password']
            user.nickname = request.POST['name']
            user.save()
            suc += 'Вы успешно зарегистрировались'
    a = {
        'suc': suc,
        'error':error
    }
    return render(request, 'reg.html', context=a)


def auth(request):
    error = ''
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login).exists() and User.objects.filter(password=password).exists():
           request.session['login'] = login
           return redirect('/panel')
        else:

            error += 'Логин или пароль error'

    a = {
        'error': error
    }
    return render(request, 'auth.html', context=a)

def article_id(request,id):
    article = Article.objects.filter(id=id).first()
    article_new = {
    'title': article.title,
    'image': str(article.image).split('/')[-1],
    'description': article.description,
    'id': article.id,
    'cat': article.category.title,
    'text': article.text
    }
    a = {
        'article':article_new
    }
    print(article_new)
    return render(request, 'article_id.html', context=a)

def panel(request):
    if not 'login' in request.session:
        return redirect('/reg')
    data = User.objects.filter(login=request.session['login']).first()

    a = {
        'data': data,
        'avatar': str(data.avatar).split('/')[-1]
    }

    if request.method == 'POST':
        nickname = request.POST['name']
        login = request.POST['login']
        password = request.POST['password']
        user = User.objects.filter(id = data.id).first()
        user.nickname = nickname
        user.login = login
        user.password = password
        user.save()
        return redirect('/panel')
    return render(request, 'panel.html', context=a)

def logout(request):
    if 'login' in request.session:
        del request.session['login']
    return redirect('/reg')

def addarticle(request):
    if request.method == 'POST' and request.FILES:
        title = request.POST['title']
        description = request.POST['description']
        text = request.POST['text']
        image = request.FILES['image']
        category = request.POST['category']
        f = FileSystemStorage()
        f.save(image.name, image)
        article = Article()
        article.title = title
        article.description = description
        article.text = text
        article.image = 'mySite/static/blog/'+image.name
        article.category = Category.objects.filter(id=category).first()
        article.save()
        request.session['suc'] = 1
    else:
        if 'suc' in request.session:
            del request.session['suc']

    form = AddArticle
    return render(request, 'addarticle.html', context={'form': form})

def users(request):
    a=User.objects.all()
    newusers = []
    for i in a:
        newusers.append({
            'id': i.id,
            'login': i.login,
            'avatar': str(i.avatar).split('/')[-1]
        })
    return render(request, 'user/users.html', context={'users': newusers})

def user_detail(request,login):
    current_user = get_object_or_404(User, login=request.session['login'])
    friend_user = get_object_or_404(User, login=login)
    if request.method == 'POST':
        if current_user == friend_user:
            return redirect('/user/'+login)
        if not Friend.objects.filter(user=current_user, friend=friend_user).exists():
            Friend.objects.create(user=current_user, friend=friend_user)
    a=User.objects.filter(login=login).first()
    newusers = {
        'id': a.id,
        'login': a.login,
        'nickname': a.nickname,
        'avatar': str(a.avatar).split('/')[-1]
    }
    f = 0
    if Friend.objects.filter(user=current_user, friend=friend_user).exists():
        f = 1

    d = 0
    if login == request.session['login']:
        d = 1
    print(d)

    return render(request, 'user/user_detail.html', context={'user': newusers, 'f': f, 'd': d})


def add_avatar(request):
    if request.method == 'POST' and request.FILES:
        image = request.FILES['avatar']

        f = FileSystemStorage()
        f.save(image.name, image)
        user_current = User.objects.filter(login=request.session['login']).first()
        user = User.objects.get(id=user_current.id)
        user.avatar = 'mySite/static/user/' + image.name
        user.save()
    return redirect('/panel')

def chat(request, login):
    current_user = get_object_or_404(User, login=request.session['login'])
    friend_user = get_object_or_404(User, login=login)
    if request.method == 'POST':
        message = request.POST['message']
        Chat.objects.create(user=current_user, friend=friend_user, message=message)

    chats = Chat.objects.filter(Q(user=current_user, friend=friend_user) | Q(user=friend_user, friend=current_user)).order_by('datetime')

    return render(request, 'user/chat.html', {'chats': chats, 'current_user': current_user, 'friend_user': friend_user})