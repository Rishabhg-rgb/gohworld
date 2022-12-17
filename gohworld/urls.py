"""gohworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from gohapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/',views.shop),
    path('shop/<str:check>/',views.shop),
    path('fetchproducts/<str:productname>/',views.fetchProductsByName),
    path('fetchproducts/<str:productName>/<str:type>/',views.FetchProducts),
    path('view/<str:type>/<int:productid>/',views.viewProduct),
    path('checkout/<str:type>/<int:productid>/',views.Checkout),
    path('search/',views.search),
    path('placeorder/<str:paymenttype>/',views.placeOrder),
    path('ordercomplete/',views.ordercomplete),
    path('register/',views.register),
    path('signup/',views.signup),
    path('login/',views.loginuser),
    path('handlelogin/',views.handlelogin),
    path('logout/',views.handlelogout),
    path('profile/',views.profile),
    path('contact/',views.contact),
    path('handlerequest/',views.handlerequest)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)