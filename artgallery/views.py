from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from .models import Categories, Painting


def index(request):
    return render(request, template_name='artgallery/index.html')


def registerPage(request):
    return render(request, 'accounts/register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password Incorrect')
            return render(request, 'accounts/login.html',)
    else:
        return render(request, 'accounts/login.html',)


def logoutUser(request):

    logout(request)
    return redirect('login')


def publications(request):

    return render(request, template_name='artgallery/publications.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email =request.POST['email']
        message =request.POST['message']

        # send email logic

        send_mail(
            'Message from' + name,
            message,
            email,
            ['nomaanahmad77@gmail.com']
        )

        return render(request, 'artgallery/contact.html', {'name': name})
    else:
        return render(request, 'artgallery/contact.html')




def aboutus(request):

    return render(request, template_name='artgallery/aboutus.html')


def gallery(request):
    painting = Painting.objects.all()
    context = {
        'painting': painting,
    }
    return render(request, 'artgallery/gallery.html', context)


def shop(request):
    forsale = Painting.objects.filter(sale='YES')
    context = {
        'forsale': forsale
    }

    return render(request, 'artgallery/shop.html', context)


def services(request):

    return render(request, template_name='artgallery/services.html')


def exhibitions(request):

    return render(request, template_name='artgallery/exhibitions.html')


def workshop(request):

    return render(request, template_name='artgallery/workshop.html')


def gallery2(request):

    return render(request, 'artgallery/gallery2.html')
