from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import FashionJewellery, PreciousJewellery, Orders, Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from itertools import chain
from decouple import config
from django.conf import settings
MERCHANT_KEY = "f5C_nrHv2rIiZL1t"
# Create your views here.


def home(request):
    print(settings.STATIC_ROOT)
    bestSellerProduct = chain(PreciousJewellery.objects.all()[
                              :2], FashionJewellery.objects.all()[:2])
    PreciousJewelleryList = PreciousJewellery.objects.all()[:4]
    FashionJewelleryList = FashionJewellery.objects.all()[:4]
    params = {"bestSellerProduct": bestSellerProduct, "preciousJewelleryList":
              PreciousJewelleryList, "fashionJewelleryList": FashionJewelleryList}
    return render(request, 'Home.html', params)


def shop(request, check=None):
    if check == None:
        preciousProductList = PreciousJewellery.objects.all().reverse()
        fashionProductList = FashionJewellery.objects.all().reverse()
        params = {'preciousProductList': preciousProductList,
                  "fashionProductList": fashionProductList}
        return render(request, 'allproducts.html', params)
    elif check != None:
        preciousProductList = PreciousJewellery.objects.filter(
            Title=check).reverse()
        fashionProductList = FashionJewellery.objects.filter(
            Title=check).reverse()
        params = {'preciousProductList': preciousProductList,
                  "fashionProductList": fashionProductList}
        return render(request, 'allproducts.html', params)


def FetchProducts(request, productName, type):
    if type == "precious":
        ProductList = PreciousJewellery.objects.filter(Title=productName)
        params = {"ProductList": ProductList}
        return render(request, "ProductList.html", params)
    elif type == "fashion":
        ProductList = FashionJewellery.objects.filter(Title=productName)
        params = {"ProductList": ProductList}
        return render(request, 'ProductList.html', params)
    else:
        return HttpResponse("error")


def viewProduct(request, type, productid):
    if type == "precious":
        product = PreciousJewellery.objects.filter(id=productid)
        params = {"product": product}
        return render(request, "view.html", params)
    if type == "fashion":
        product = FashionJewellery.objects.filter(id=productid)
        params = {"product": product}
        return render(request, "view.html", params)


def Checkout(request, type, productid):
    if type == "precious":
        product = PreciousJewellery.objects.filter(id=productid)
        params = {"product": product}
        return render(request, "checkout.html", params)
    if type == "fashion":
        product = FashionJewellery.objects.filter(id=productid)
        params = {"product": product}
        return render(request, "checkout.html", params)


def fetchProductsByName(request, productname):
    ProductList = FashionJewellery.objects.filter(Title=productname).reverse()
    params = {"ProductList": ProductList}
    return render(request, "shop.html", params)


def search(request):
    query = request.GET['searchquery'].lower()
    preciousProductList = PreciousJewellery.objects.filter(Title=query)
    fashionProductList = FashionJewellery.objects.filter(Title=query)
    params = {'preciousProductList': preciousProductList,
              "fashionProductList": fashionProductList}
    return render(request, 'Searchshop.html', params)


def placeOrder(request, paymenttype):
    if request.method == "POST":
        if paymenttype == "onlinepayment":
            items = request.POST['items']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phoneno = request.POST['phonenumber']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            zip = request.POST['zip']
            amount = request.POST['amount']
            SKU = request.POST['SKU']
            order = Orders(name=firstname+lastname, email=email, address=address,
                           city=city, state=state, zip_code=zip, phoneno=phoneno, items=items, amount=amount, SKU=SKU, paymentmethod=paymenttype)
            order.save()
            # request paytm to transfer the amount to your account after payment by user
            param_dict = {
                'MID': 'njFFHP14483068680155',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
                param_dict, MERCHANT_KEY)
            return render(request, 'paytm.html', {'param_dict': param_dict})
        elif paymenttype == "COD":
            items = request.POST['items']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phoneno = request.POST['phonenumber']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            zip = request.POST['zip']
            amount = request.POST['amount']
            SKU = request.POST['SKU']
            order = Orders(name=firstname+lastname, email=email, address=address,
                           city=city, state=state, zip_code=zip, phoneno=phoneno, items=items, amount=amount, SKU=SKU, paymentmethod=paymenttype)
            order.save()
            return redirect('/ordercomplete')

    return HttpResponse("eor")


def ordercomplete(request):
    return render(request, 'order-complete.html')


def register(request):
    return render(request, 'register.html')


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        phonenumber = request.POST['phonenumber']
        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.first_name = name
            user.last_name = phonenumber
            user.save()
            return redirect('/')
        else:
            return HttpResponse("Error 404 BAD REQUEST")
    return redirect('/')


def loginuser(request):
    return render(request, 'login.html')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("user not registered")


def handlelogout(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'register.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        mycontact = Contact(name=name, email=email, query=query)
        mycontact.save()

        return render(request, 'query-send.html')
    elif request.method == "GET":
        return render(request, "contact.html")


@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        # Here paytm send post request here
        form = request.POST
        response_dict = {}
        for i in form.keys():
            response_dict[i] = form[i]
            if i == 'CHECKSUMHASH':
                checksum = form[i]

        verify = Checksum.verify_checksum(
            response_dict, MERCHANT_KEY, checksum)
        if verify:
            if response_dict['RESPCODE'] == '01':
                print("Order Successful")
            else:
                print("order was not successful" + response_dict['RESPMSG'])
        return render(request, 'paymentstatus.html', {'response': response_dict})

    return redirect('/')
