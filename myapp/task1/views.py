from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import UserRegister
from .models import *


# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def news(request):
    news_pag = News.objects.all().order_by('-date')
    paginator = Paginator(news_pag, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})


def products(request):
    game_data = Game.objects.all().values()

    context = {
        "head": "Асортимент игр",
        "services": game_data,
    }
    return render(request, 'products.html', context)


def basket(request):
    return render(request, 'basket.html', {'images': None})


#     try:
#         # Example data; replace with your actual data
#         images = [
#             {'image_url': 'images/image1.jpg', 'caption': 'Маникюр 1'},
#             {'image_url': 'images/image2.jpg', 'caption': 'Маникюр 2'},
#         ]
#         # Crucial step to use the static file system:
#         image_files = [os.path.join('static', i['image_url']) for i in images]
#
#         # Make sure you have your photo folder inside the static folder
#         # and static folder in your root django project
#         return render(request, 'basket.html', {'images': images})
#
#     except FileNotFoundError:
#         return render(request, 'basket.html', {'images': None})


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:

                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'

        else:
            info['error'] = form.errors
            info['form'] = form

    else:
        info['form'] = UserRegister()

    return render(request, 'registration_page.html', {'info': info})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        try:
            age = int(request.POST.get('age'))
        except (ValueError, TypeError):
            age = -1

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, balance=0, age=age)
            info['message'] = f'Приветствуем, {username}!'

    return render(request, 'registration_page.html', {'info': info})
