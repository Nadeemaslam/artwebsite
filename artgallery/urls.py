from django.urls import path
# from artgallery.views import registerPage, loginPage, logoutUser
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('about_us/', views.aboutus, name='aboutus'),
    path('publications/', views.publications, name='publications'),
    # path('logout/', logoutUser, name='logout'),
    path(r'contact/', views.contact, name='contact'),
    path(r'shop/', views.shop, name='shop'),
    path(r'services/', views.services, name='services'),
    path(r'exhibitions/', views.exhibitions, name='exhibitions'),
]