"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import index, register
from django.contrib.auth.views import login, logout_then_login
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index, name='index'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', logout_then_login, name='logout'),
    url(r'^$', index, name='index'),
    url(r'^mooc/', include('mooc.urls')),
    url(r'^index/show', 'mooc.views.show_my_course', name='show_my_course'),

]
