from django.template.context_processors import static
from django.urls import path
from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    path('', index),
    url('index', views.index, name='index'),
    url('products', views.products, name='products'),
    url('reg', views.reg, name='reg'),
    url('signin', views.signin, name='signin'),
    url('orders', views.orders, name='orders'),

]