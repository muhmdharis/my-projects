from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from fuzzywuzzy import process
from django.http import JsonResponse



def home(request):
    u = request.user
    return render(request, 'app/home.html', {'u': u})


def wallet(request):
    u = request.user
    user = User.objects.get(username=u)
    try:
        wallet = Wallet.objects.get(user = u)
    except:
        wallet = Wallet.objects.create(user=u, totalAmount=0)

    #if request.method == 'POST':
        #withdraw_amount = request.POST.get('withdraw')
        #if withdraw_amount:
            #withdraw_amount = int(withdraw_amount)
            #if wallet.totalAmount >= withdraw_amount:
                #wallet.totalAmount -= withdraw_amount
                #wallet.save()

    if user.is_superuser:
        try:
            history = History.objects.all()
            context = {
                'u':u,
                'historys':history,
                'wallet':wallet
            }
        except:
            context = {
                'u':u,
                'wallet':wallet,
            }
    else:
        try:
            Userhistory = HistoryExchange.objects.filter(user=user,startDate__isnull=True)
            print(Userhistory)
            context = {
                'u':u,
                'Userhistorys':Userhistory,
                'wallet':wallet
            }
        except:
            context = {
                'u':u,
                'wallet':wallet,
            }

    return render(request, 'app/wallet.html', context)

def register(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        e = request.POST.get('e')
        m = request.POST.get('m')
        l = request.POST.get('l')
        print(u, p)
        if User.objects.filter(username=u).exists():
             return render(request, 'app/register.html',{'msg':'username already exists'})
        else:
            User.objects.create_user(username=u, email=e, password=p, first_name=m, last_name=l,is_active=False).save()
            return redirect(loginn)
        
    return render(request, 'app/register.html')


def loginn(request):
    if request.method == 'POST':
        u = request.POST.get('u')
        p = request.POST.get('p')
        # print(u)
        n = authenticate(request, username=u, password=p)
        # if User.objects.filter(username=u).exists():
        #     print(n)
        user = User.objects.filter(username=u).exists()

        if user:
            user_check = User.objects.get(username=u)

            if n and n.is_active == 1:
                login(request, n)
                return redirect(home)

            if user_check.is_active == 0:
                return JsonResponse({"status": "error", "msg": "User is not approved by the admin"})

            if not n:
                return JsonResponse({"status": "error", "msg": "Incorrect Password"})
        else:
            return JsonResponse({"status": "error", "msg": "User is not Registered"})

    return render(request, 'app/login.html')


def logoutt(request):
    logout(request)
    return redirect(loginn)


def sell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        email = request.POST.get('email')
        discription = request.POST.get('discription')
        image = request.FILES.get('image')

        product.objects.create(name=name, model=model, email=email, price=discription, img=image).save()
        return redirect(home)
    return render(request, 'app/sell.html')


def verifyy(request):
    user = User.objects.filter(is_active=False)
    return render(request, 'app/verify.html',{'object':user})


def ver(request, id=id):
    user=User.objects.get(pk=id)
    user.is_active = True
    user.save()
    return redirect(verifyy)


def buy(request):
    user = request.user
    u = User.objects.get(username=user)
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', '')

    products = product.objects.all()

    if query:
        product_names = [product.name for product in products]
        matched_names = process.extract(query, product_names, limit=10)
        matched_names = [name for name, score in matched_names if score > 50]
        products = products.filter(name__in=matched_names)

    if filter_type == 'price_low_high':
        products = products.order_by('price')
    elif filter_type == 'price_high_low':
        products = products.order_by('-price')
    elif filter_type == 'alphabetical':
        products = products.order_by('name')

    return render(request, 'app/buy.html', {'n': products, 'query': query, 'filter_type': filter_type,'u':u})


def b(request, id=id):
    n = get_object_or_404(product, id=id)
    return render(request, 'app/b.html', {'n': n})

def deleteProduct(request, id=id):
    n = get_object_or_404(product, id=id)
    n.delete()
    return redirect('buy')


def exchangee(request):
    n = exchange.objects.filter(isActive='waiting')
    user = request.user
    
    if request.method == 'POST':
        name = request.POST.get('n')
        model = request.POST.get('m')
        email = request.POST.get('e')
        expected_price = request.POST.get('d')
        image = request.FILES.get('image')
        
        new_exchange = exchange.objects.create(
            user=user,
            name=name,
            model=model,
            email=email,
            exprectedPrice=expected_price,
            img=image
        )
        
        HistoryExchange.objects.create(
            user=user,
            Exchangeitem=new_exchange, 
            exchangeDate=datetime.now().strftime("%Y-%m-%d"), 
            exchangeRate=int(expected_price) 
        )
        
        return redirect('exchange') 
    
    return render(request, 'app/exchange.html', {'n': n, 'u': user})

def delete_product(request, id):
    product = get_object_or_404(exchange, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('exchange')
    
def approveExchange(request, id):
    product = get_object_or_404(exchange, id=id)
    user = User.objects.get(id=product.user.id)
    wallet, created = Wallet.objects.get_or_create(user=user)
    price = product.exprectedPrice
    price = int(price)
    wallet.totalAmount += price
    wallet.save()
    product.isActive = 'True'
    product.save()
    return redirect('exchange')

def rejectExchange(request, id):
    product = get_object_or_404(exchange, id=id)
    product.isActive = 'False'
    product.save()
    return redirect('exchange')


def chatt(request):
    p = 'admin'
    if request.user.username == p:
        n = chat.objects.all()
        m = 'p'
        return render(request, 'app/chat.html', {'n': n, 'm': m})
    else:
        n = chat.objects.filter((Q(user__username=request.user.username) & Q(t='admin')) |
                                (Q(user__username='admin') & Q(t=request.user.username)))
        if request.method == 'POST':
            m = request.POST.get('m')
            chat.objects.create(user=request.user, message_f=m, t='admin').save()

            return redirect(chatt)

        return render(request, 'app/chat.html', {'n': n, 'm': 'no obj'})


def delete_chat_msg(request, id):
    if request.user.is_superuser:
        chat.objects.get(id=id).delete()

    return redirect("chat")


def c(request, id):
    n = chat.objects.filter(user__id=id)
    t = chat.objects.filter(user__id=id).first()
    print(t.user.username)
    if request.method == 'POST':
        m = request.POST.get('m')
        chat.objects.create(user=request.user, message_f=m, t=t.user.username).save()
        return redirect(chatt)
    return render(request, 'app/c.html', {'n': n})


def ec(request, id=id):
    p = get_object_or_404(exchange, id=id)
    cart.objects.create(user=request.user, name=p.name, model=p.model, email=p.email, discription=p.discription).save()
    return redirect(home)


def cartt(request, id=id):
    p = get_object_or_404(product, id=id)
    cart.objects.create(user=request.user, productName= p).save()
    return redirect(home)


def ca(request, id=id):
    """Cart page"""

    n = cart.objects.filter(user__username=request.user.username)
    return render(request, 'app/ca.html', {'n': n})

# def ca(request):
#     """Cart page"""

#     n = cart.objects.filter(user__username=request.user.username)
#     return render(request, 'app/ca.html', {'n': n})


def dc(request, id=id):
    print(id)
    n = get_object_or_404(cart, id=id)
    n.delete()
    return redirect(ca, n.user.id)


def o(request, id=id):
    """Shipping address page"""
    user = request.user
    item = get_object_or_404(cart, id=id) 
    originalRate = int(item.productName.price)  

    wallet, created = Wallet.objects.get_or_create(user=user)
    totalAmountUserHave = wallet.totalAmount
    userHaveToPay = originalRate

    if totalAmountUserHave > 0:
        userHaveToPay = max(originalRate - totalAmountUserHave, 0)
        wallet.totalAmount = max(wallet.totalAmount - originalRate, 0)
        wallet.save()
        print(totalAmountUserHave)
        print(userHaveToPay)
    
    flag = 0 if totalAmountUserHave > 0 else 1
    
    if request.method == 'POST':
        return redirect('placed')  

    return render(request, 'app/orr.html', {
        'n': id,
        'user': user,
        'flag': flag,
        'item': item,
        'userHaveToPay': userHaveToPay
    })


def premium(request, id=id):
    user = request.user
    print(user.id)
    try:
        history = History.objects.get(user=user)
    except History.DoesNotExist:
        history = History.objects.create(user=user, premiumState='False')
    if request.method == 'POST':
        user = get_object_or_404(User, pk=id)
        userHis, created = History.objects.get_or_create(user=user)
        userHis.premiumState = 'True'
        userHis.startDate = datetime.today()
        userHis.save()
        adminUser = get_object_or_404(User, is_superuser=True)
        wallet, created = Wallet.objects.get_or_create(user=adminUser)
        wallet.totalAmount += 199
        wallet.save()
        return redirect('home')
    
    return render(request, 'app/premium.html', {'n': id,'user':history})

def back(request):
    return redirect('ca')


def orderr(request, id=id):
    p = get_object_or_404(cart, id=id)
    n = p
    p.delete()
    order_item = order.objects.create(user=request.user, name=n.productName.name, model=n.productName.model,
                                      email=n.productName.email, discription=n.productName.price)
    order_item.save()

    # email
    date = datetime.now().date()
    time = datetime.now().time().replace(second=0, microsecond=0)
    msg = "The order you placed on {date} {time} is successful. \nItem: Name: {order_item.name} Model: {order_item.model}"

    html_msg = render_to_string(
        "app/email_template.html",
        context={
            "name": order_item.user.username,
            "item_name": order_item.name,
            "item_model": order_item.model,
            "item_price": order_item.discription,
            "time": f"{date} {time}"
        }
    )

    send_mail(
        subject="Order Successful", message=msg, from_email=None,
        recipient_list=[order_item.user.email],
        html_message=html_msg
    )

    return redirect(ca, n.user.id)


def ord(request, id=id):
    n = order.objects.filter(user__id=id)
    return render(request, 'app/or.html', {'n': n})


def orde(request, id=id):
    n = order.objects.all()
    return render(request, 'app/ord.html', {'n': n})


def od(request, id=id):
    n = get_object_or_404(order, id=id)
    n.delete()
    return redirect(home)


def placed(request, id=id):
    return render(request, 'app/placed.html', {'n': id})


def de(request):
    n = User.objects.exclude(id=1)
    return render(request, 'app/de.html', {'n': n})


def ud(request, id=id):
    n = get_object_or_404(User, id=id)
    n.delete()
    return redirect(de)


def about(request):
    return render(request, 'app/about.html')
