from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from el_shops.models import Product, Categories, Filter_Price, Color, Brand, Contact_us
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


def BASE(request):
    return render(request, 'Main/base.html')


def HOME(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'Main/index.html', context)


def PRODUCT(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    brand = Brand.objects.all()
    color = Color.objects.all()
    FILTER_PRICE_ID = request.GET.get('filter_price')
    CATID = request.GET.get('categories')
    COLORID = request.GET.get('color')
    BRANDID = request.GET.get('brand')
    ATOZID = request.GET.get('ATOZ')
    ZTOAID = request.GET.get('ZTOA')
    PRICE_LOWTOHIGHTID = request.GET.get('PRICE_LOWTOHIGHT')
    PRICE_HIGHTTOLOWID = request.GET.get('PRICE_HIGHTTOLOW')
    NEW_PRODUCTID = request.GET.get('NEW_PRODUCT')
    OLD_PRODUCTID = request.GET.get('OLD_PRODUCT')

    if CATID:
        product = Product.objects.filter(categories=CATID, status='Publish')
    elif FILTER_PRICE_ID:
        product = Product.objects.filter(filter_price=FILTER_PRICE_ID)
    elif COLORID:
        product = Product.objects.filter(color=COLORID, status='Publish')
    elif BRANDID:
        product = Product.objects.filter(color=BRANDID, status='Publish')
    elif ATOZID:
        product = Product.objects.filter(status='Publish').order_by('name')
    elif ZTOAID:
        product = Product.objects.filter(status='Publish').order_by('-name')
    elif PRICE_LOWTOHIGHTID:
        product = Product.objects.filter(status='Publish').order_by('price')
    elif PRICE_HIGHTTOLOWID:
        product = Product.objects.filter(status='Publish').order_by('-price')
    elif PRICE_HIGHTTOLOWID:
        product = Product.objects.filter(
            status='Publish', condition='New').order_by('-id')
    elif OLD_PRODUCTID:
        product = Product.objects.filter(
            status='Publish', condition='Old').order_by('-id')
    else:
        product = Product.objects.filter(status='Publish')
    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,
    }
    return render(request, 'Main/product.html', context)


def SEARCH(request):
    return render(request, 'Main/search.html')


def PRODUCT_DETAIL_PAGE(request, id):
    prod = Product.objects.filter(id=id).first()

    context = {
        'prod': prod,
    }

    return render(request, 'Main/product_single.html', context)


def Contact_Page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_us = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact_us.save()
        # subject=subject
        # message=message
        # email_from=settings.EMAIL_HOST_USER
        # try:
        #     send_mail(subject,message,email_from, ['qoziyevsharofiddin199805@gmail.com'])
        #     contact_us.save()
        #     return redirect('home')
        # except:
        #     return redirect('contact')

    return render(request, 'Main/contact.html')


def HandleRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('home')

    return render(request, 'Registration/auth.html')


def HandleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'Registration/auth.html')


def HandleLogout(request):
    logout(request)
    return redirect('home')
    return render(request, 'Main/index.html')

# Cart


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'Cart/cart_details.html')


def Check_out(request):
    return render(request, 'Cart/checkout.html')
