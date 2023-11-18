from django.shortcuts import render, redirect
from mySite.models import Article, User
from  mySite.forms import AddArticle
from django.core.files.storage import FileSystemStorage
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
            'cat':article.category.title
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
        'data': data
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
        print(image)
        category = request.POST['category']
        f = FileSystemStorage()
        f.save('image', image)
        url_file = f.url()

        '''article = Article()
        article.title = title
        article.description = description
        article.text = text
        article.image = url_file
        article.category = category
        article.save()
        return redirect('addarticle')'''


    else:
        form = AddArticle
    return render(request, 'addarticle.html', context={'form': form})