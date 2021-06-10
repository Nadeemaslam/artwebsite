from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect


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



def contact(request):

    return render(request, template_name='artgallery/contact.html')


def products(request):
    return render(request, template_name='artgallery/products.html')