from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Product, Order, OrderProducts
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import *
import datetime
import time

def index(request):
    if str(User.objects.filter(pk=request.user.id)) != "<QuerySet []>":
        username = str(User.objects.get(pk=request.user.id).first_name) + " " + str(
            User.objects.get(pk=request.user.id).last_name)
    else:
        username = ""
    print(username)
    return render(request, 'ferm/index.html',{'username':username})


def peresech(sp1, request):
    for item in sp1:
        if str(item.pk) in request.POST:
            lol = item.pk
            return lol
        else:
            lol = None
    return lol


def products(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        # for item in Product.objects.all():
        #     print(str(item.pk))
        #     if str(item.pk) in request.POST:
        #         print("AAAAAAAAAAAAAAAAAAAAAA")
        #     else:
        #         print("BBBBBBBBBBBBBBBBBBBBBB")
        if form.is_valid():
            count = form.cleaned_data['Count']
            if count<0:
                form = OrderForm()
                messages.error(request, 'Вводите только положительные числа!!')
                return render(request, 'ferm/products.html', {'products': products,
                                                              'form': form})
            print(count)
            if str(Order.objects.filter(ClientId=User.objects.get(pk=request.user.id),
                                        DateOfRegistration=None)) != "<QuerySet []>":
                order = Order.objects.get(ClientId=User.objects.get(pk=request.user.id), DateOfRegistration=None)
                isNewOrder=False
            else:
                order = Order.objects.create(ClientId=User.objects.get(pk=request.user.id), DateOfRegistration=None)
                isNewOrder=True
            productID = peresech(Product.objects.all(), request)
            productPrice = Product.objects.get(pk=productID).Price
            if str(OrderProducts.objects.filter(OrderID=order.pk, ProductID=productID)) != "<QuerySet []>":
                print(str(OrderProducts.objects.filter(OrderID=order.pk, ProductID=productID)))
                orderProduct = OrderProducts.objects.get(OrderID=Order.objects.get(pk=order.pk),
                                                         ProductID=Product.objects.get(pk=productID))


                if Product.objects.get(pk=productID).Count < count +orderProduct.Count:
                    form = OrderForm()
                    messages.error(request, 'Слишком много захотел!')
                    if isNewOrder:
                        order.delete()
                    return render(request, 'ferm/products.html', {'products': products,
                                                                  'form': form})


                orderProduct.Count += count
                orderProduct.Cost = orderProduct.Price * orderProduct.Count
                OrderProducts.objects.filter(pk=orderProduct.pk).update(Count=orderProduct.Count,Cost=orderProduct.Cost)
            else:
                orderProduct = OrderProducts.objects.create(OrderID=Order.objects.get(pk=order.pk),
                                                            ProductID=Product.objects.get(pk=productID),
                                                            Count=count,
                                                            Price=productPrice,
                                                            Cost=count * productPrice,
                                                            Kind=Product.objects.get(pk=productID).Kind)

                if Product.objects.get(pk=productID).Count < count + orderProduct.Count:
                    form = OrderForm()
                    messages.error(request, 'Слишком много захотел!')
                    if isNewOrder:
                        order.delete()
                    orderProduct.delete()
                    return render(request, 'ferm/products.html', {'products': products,
                                                                  'form': form})

                orderProduct.Cost = orderProduct.Price * orderProduct.Count
                OrderProducts.objects.filter(pk=orderProduct.pk).update(Cost=orderProduct.Cost)
            sumOf = 0
            for op in OrderProducts.objects.all():
                if order.pk == op.OrderID.pk:
                    sumOf += op.Cost
            Order.objects.filter(pk=order.pk).update(Cost=sumOf)

    else:
        form = OrderForm()
    if str(User.objects.filter(pk=request.user.id))!="<QuerySet []>":
        username= str(User.objects.get(pk=request.user.id).first_name)+" "+str(User.objects.get(pk=request.user.id).last_name)
    else:
        username=""
    return render(request, 'ferm/products.html', {'products': products,
                                                  'form': form,
                                                  'username':username})


def reg(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрированы!')
            return redirect('signin')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    if str(User.objects.filter(pk=request.user.id))!="<QuerySet []>":
        username= str(User.objects.get(pk=request.user.id).first_name)+" "+str(User.objects.get(pk=request.user.id).last_name)
    else:
        username=""
    return render(request, 'ferm/reg.html', {
        'form': form,
        'username':username
        })


def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products')
    else:
        form = UserLoginForm()

    if str(User.objects.filter(pk=request.user.id))!="<QuerySet []>":
        username= str(User.objects.get(pk=request.user.id).first_name)+" "+str(User.objects.get(pk=request.user.id).last_name)
    else:
        username=""
    return render(request, 'ferm/signin.html', {'form': form,
                                                'username':username
                                                })


def orders(request):
    if request.method == 'POST':
        if str(Order.objects.filter(ClientId=User.objects.get(pk=request.user.id),
                                    DateOfRegistration=None)) != "<QuerySet []>":
            order = Order.objects.get(ClientId=User.objects.get(pk=request.user.id), DateOfRegistration=None)
            for item in OrderProducts.objects.all():
                if order.pk == item.OrderID.pk:
                    if str(item.Kind) in request.POST:
                        item.delete()
                        #Пересчет итого:
                        sumOfOrder = 0
                        for op in OrderProducts.objects.all():
                            if order.pk == op.OrderID.pk:
                                sumOfOrder += op.Cost
                        Order.objects.filter(pk=order.pk).update(Cost=sumOfOrder)
                        messages.info(request, 'Товар из заказа удален')

                    if str(order.pk) in request.POST:
                        Order.objects.filter(pk=order.pk).update(DateOfRegistration=time.strftime("%Y-%m-%d"))
                        messages.success(request, 'Заказ успешно оформлен!!')
    if str(Order.objects.filter(ClientId=User.objects.get(pk=request.user.id),
                                DateOfRegistration=None)) != "<QuerySet []>":
        order = Order.objects.get(ClientId=User.objects.get(pk=request.user.id), DateOfRegistration=None)
        ordersIsExist =True
        ordPK=order.pk
    else:
        order = None
        ordersIsExist=False
        ordPK=-1
    order_products = []
    print(order)
    kolvo = 0
    if ordersIsExist:
        for op in OrderProducts.objects.all():
            if order.pk == op.OrderID.pk:
                kolvo += 1
        if kolvo == 0:
            ordersIsExist = False

    if ordersIsExist:
        for op in OrderProducts.objects.all():
            if order.pk == op.OrderID.pk:
                order_products.append(op)

    if str(User.objects.filter(pk=request.user.id))!="<QuerySet []>":
        username= str(User.objects.get(pk=request.user.id).first_name)+" "+str(User.objects.get(pk=request.user.id).last_name)
    else:
        username=""
    return render(request, 'ferm/orders.html', {
        'order':order,
        'orderPK':ordPK,
        'ordersIsExist':ordersIsExist,
        'order_products':order_products,
        'username': username
    })
