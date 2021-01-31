from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.
from sales.form import *
from sales.models import CustomUser


def index(request):
    return render(request, 'sales/index.html')


def login(request):
    return render(request, 'sales/login.html')


def login_views(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('success')
            else:
                return redirect('sorry')
        except auth.ObjectDoesNotExist:
            print("invalid user")
    return render(request, 'sales/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'sales/login.html')


def success(request):
    return render(request, 'sales/success.html')


def sorry(request):
    return render(request, 'sales/sorry.html')


def shop_sign(request):
    return render(request, 'sales/shop_sign_up.html')


def shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                email = request.POST.get('email')
                password = request.POST.get("password")
                shop = form.save()
                use = CustomUser.objects.create(username=email, is_shop=True)
                use.set_password(password)
                use.save()
                idi = use.id
                print(idi)
                shop.CustomUser_id = CustomUser.objects.get(id=idi)
                shop.save()
                return redirect('login')
            except:
                pass
    else:
        form = ShopForm()
    return render(request, 'sales/shop_sign_up.html', {'form': form})


def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('productshow')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'sales/product/product_new.html', {'form': form})


def productshow(request):
    products = Product.objects.all()
    return render(request, 'sales/product/product_list.html', {'products': products})


def productedit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'sales/product/product_edit.html', {'product': product})


def productupdate(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
    product = Product.objects.all()
    return render(request, 'sales/product/product_list.html', {'products': product})


def productdestroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('productshow')


def offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('offershow')
            except:
                pass
    else:
        form = OfferForm()
    return render(request, 'sales/offer/offer_new.html', {'form': form})


def offershow(request):
    offers = Offer.objects.all()
    return render(request, 'sales/offer/offer_list.html', {'offers': offers})


def offeredit(request, id):
    offer = Offer.objects.get(id=id)
    return render(request, 'sales/offer/offer_edit.html', {'offer': offer})


def offerupdate(request, id):
    offer = Offer.objects.get(id=id)
    form = OfferForm(request.POST, request.FILES or None, instance=offer) #added
    if form.is_valid():
        form.save()
    offer = Offer.objects.all()
    return render(request, 'sales/offer/offer_list.html', {'offers': offer})


def offerdestroy(request, id):
    offer = Offer.objects.get(id=id)
    offer.delete()
    return redirect('offershow')


def search_product(request):
    if request.method == "POST":
        if request.POST['keyword_product']:
            form = ProductSearchForm(request.POST)
            if form.is_valid():
                key = form.cleaned_data['keyword_product']
                print(key)
                v = form.cleaned_data['product_column']
                if v == 'item':
                    comp = Product.objects.filter(product_name__icontains=key)
                elif v == 'price':
                    comp = Product.objects.filter(price__exact=key)
                elif v == 'discount':
                    comp = Product.objects.filter(discount__exact=key)
            co = comp.count()
            context = {'products': comp, 'count': co}
            return render(request, 'sales/product/product_list.html', context)
    return redirect('productshow')

