"""
URL configuration for mysite project.
cd ./mysite\

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from .views import contact # type: ignore     


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homePage, name="home"), 
    path('about-us/',views.aboutus, name="about-us"),
    path('prewedding/',views.prewedding, name="prewedding"),
    path('wedding/',views.wedding, name="wedding"),
    path('maternity/',views.maternity, name="maternity"),
    path('films/',views.films, name="films"),
    path('contact-us/',views.contact, name="contact-us"), 
    path('terms & conditions/',views.terms, name="terms & conditions"), 
    path('saveenquiry/',views.saveEnquiry, name="saveenquiry"),
    path('page1/',views.a, name="page1"),
    path('page2/',views.b, name="page2"),
    path('page3/',views.c, name="page3"),
    path('page4/',views.d, name="page4"),
    path('page5/',views.e, name="page5"),
    path('page6/',views.f, name="page6"),
    path('page7/',views.g, name="page7"),
    path('page8/',views.h, name="page8"),
    path('page9/',views.i, name="page9"),
    path('page10/',views.j, name="page10"),
    path('page11/',views.k, name="page11"),
    path('page12/',views.l, name="page12"),
]


