from django.urls import path
# from artgallery.views import registerPage, loginPage, logoutUser
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('products/', views.products, name='products'),
    # path('register/', registerPage, name='register'),
    # path('login/', loginPage, name='login'),
    # path('logout/', logoutUser, name='logout'),
    # path(r'contact/', views.contact, name='contact'),
]