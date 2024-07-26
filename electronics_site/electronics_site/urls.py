"""
URL configuration for online_moobile project.

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
from app import views
from django.conf import settings 
from django.urls import path, include 
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginn, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logoutt,name="logout"),
    path('de',views.de,name="de"),
    path('ud/<int:id>',views.ud,name="ud"),
    path('home',views.home,name="home"),
    path('sell',views.sell,name="sell"),
    path('verify',views.verifyy,name="verify"),
    path('verify/<int:id>',views.ver,name="ver"),
    path('buy',views.buy,name="buy"),
    path('wallet',views.wallet,name="wallet"),
    path('buy/<int:id>',views.b,name="b"),
    path('cart/<int:id>',views.cartt,name="cart"),
    path('deleteProduct/<int:id>',views.deleteProduct,name="deleteProduct"),
    path('exchange',views.exchangee,name="exchange"),
    path('back',views.back,name="back"),
    path('chat',views.chatt,name="chat"),
    path('delete_message/<int:id>', views.delete_chat_msg, name="delete_chat_msg"),
    path('ord',views.orde,name="ord"),
    path('c/<int:id>',views.c,name="c"),
    path('ca/<int:id>',views.ca,name="ca"),
    path('ca',views.ca,name="ca"),
    path('ec/<int:id>',views.ec,name="ec"),
    path('dc/<int:id>',views.dc,name="dc"),
    path('premium/<int:id>',views.premium,name="premium"),
    path('order/<int:id>',views.orderr,name="order"),
    path('ord/<int:id>',views.ord,name="ord"),
    path('o/<int:id>',views.o,name="o"),
    path('od/<int:id>',views.od,name="od"),
    path('placed',views.placed,name="placed"),
    path('about',views.about,name="about"),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('approveExchange/<int:id>/', views.approveExchange, name='approveExchange'),
    path('rejectExchange/<int:id>/', views.rejectExchange, name='rejectExchange'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)