from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from platform import uname
from platform import uname
import razorpay

from Adminapp.models import ProductDB, PerfumeDB, ContactDB, RegisterDB, CartDb, OrderDB,ClientDB


# Create your views here.
def Home(request):
    client=ClientDB.objects.all()
    categories = PerfumeDB.objects.all()
    feature= PerfumeDB.objects.all()[:1]
    product = PerfumeDB.objects.all()

    cart_total = 0
    uname =request.session.get('Username')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()


    return render(request,'Home.html',{'product':product,'feature':feature,'categories':categories,'client':client,'cart_total':cart_total})
def About(request):
    feature = PerfumeDB.objects.filter()[:1]
    categories = PerfumeDB.objects.all()
    return render(request,'About.html',{'categories':categories,'feature':feature})
def product(request):
    categories = PerfumeDB.objects.all()
    product = ProductDB.objects.all()
    return render(request,'Product.html',{'product':product,'categories':categories})
def filtered_product(request,cat_name):
    product = ProductDB.objects.filter(category_name=cat_name)
    categories = PerfumeDB.objects.all()
    return render(request, 'single_product.html', {'product': product,'categories':categories})
def terms(request):
    feature = PerfumeDB.objects.filter()[:1]
    categories = PerfumeDB.objects.all()
    return render(request,'terms.html',{'categories':categories,'feature':feature})
def contact(request):
    return render(request,'contact.html')
def save_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("Email")
        subject = request.POST.get("Subject")
        message = request.POST.get("Message")
        PhoneNO = request.POST.get("PhoneNO")
        obj =ContactDB(name=name,Email=email,Subject=subject,Message=message,PhoneNO=PhoneNO)
        obj.save()
        return redirect(contact)

def main_page(request):
    feature = PerfumeDB.objects.all()[:3]
    return render(request,"Main_page.html",{'feature':feature})
def Single_iteam(request,pro_id):
    PERFUMES = ProductDB.objects.all()[:6]
    products = ProductDB.objects.get(id=pro_id)
    return render(request,'filtered_Single.html',{'products':products,'PERFUMES':PERFUMES})

def User_register(request):
    feature = PerfumeDB.objects.all()
    return render(request,'Registration.html',{'feature':feature})
def save_register(request):
    if request.method == "POST":
        Username = request.POST.get("Username")
        Email = request.POST.get("Email")
        Password = request.POST.get("Password")
        Confirm_Password = request.POST.get("Confirm_Password")
        if RegisterDB.objects.filter(Username=Username).exists():
            print("user already exists")
            return redirect(User_register)

        elif RegisterDB.objects.filter(Email=Email).exists():
            print("Email Already Exists")
            return redirect(User_register)
        elif Password != Confirm_Password:
            print("Passwords do not match")
            return redirect(User_register)
        else:
            obj = RegisterDB(
                Username=Username,
                Email=Email,
                Password=make_password(Password),
                Confirm_Password=make_password(Confirm_Password),
            )
            obj.save()
            return redirect(User_register)
    return redirect(User_register)
def user_login(request):
    if request.method=="POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        user = RegisterDB.objects.filter(Username=Username).first()
        password_matches = False
        if user:
            password_matches = check_password(Password, user.Password) or user.Password == Password
        if password_matches:
            request.session['Username']=Username
            return redirect(Home)
        else:
            print("Username doesn't exist..! ")
            return redirect(User_register)
    else:
        print("Invalid Login...!")
        return redirect(User_register)
def user_logout(request):
    request.session.pop('Username', None)
    request.session.pop('Password', None)
    return redirect(Home)
def Cart_page(request):
    products = CartDb.objects.filter(Username=request.session.get("Username"))
    category = PerfumeDB.objects.all()
    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    for i in products:
        sub_total += i.TotalPrice or 0
    if sub_total:
        delivery_charge = 0 if sub_total > 1000 else 100
        total_amount = sub_total + delivery_charge
    return render(request,'Cart.html',{'products':products,'category':category,'sub_total':sub_total,'delivery_charge':delivery_charge,'total_amount':total_amount})
def save_to_cart(request, pro_id):
    if request.method == "POST":
        if not request.session.get("Username"):
            return redirect(User_register)
        products = get_object_or_404(ProductDB, id=pro_id)
        Quantity = max(int(request.POST.get("Quantity") or 1), 1)
        Username = request.session.get("Username")
        price = int(products.price)
        total = price * Quantity
        img = products.product_Image
        obj = CartDb(product_name=products.product_name,Username=Username,Quantity=Quantity,price=price,TotalPrice=total,Prod_Image=img)
        obj.save()
    return redirect(Home)
def Check_out_page(request):
    products = CartDb.objects.filter(Username=request.session.get("Username"))
    sub_total = sum((i.TotalPrice or 0) for i in products)
    delivery_charge = 0 if sub_total > 1000 else 100
    total_amount = sub_total + delivery_charge if sub_total else 0
    return render(request, 'check_out.html', {
        'products': products,
        'sub_total': sub_total,
        'delivery_charge': delivery_charge,
        'total_amount': total_amount,
    })


def save_check_out(request):
    if request.method == "POST":
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Email = request.POST.get('Email')
        Place = request.POST.get('Place')
        Address = request.POST.get('Address')
        Mobile = request.POST.get('Mobile')
        State = request.POST.get('State')
        pin = request.POST.get('pin')
        cart_items = CartDb.objects.filter(Username=request.session.get("Username"))
        sub_total = sum((i.TotalPrice or 0) for i in cart_items)
        delivery_charge = 0 if sub_total > 1000 else 100
        Total_price = sub_total + delivery_charge if sub_total else 0
        if Total_price <= 0:
            return redirect(Cart_page)
        obj = OrderDB(First_Name=First_Name, Last_Name=Last_Name,Email=Email,Place=Place,Address=Address,Mobile=Mobile,State=State,pin=pin,Total_price=Total_price )
        obj.save()
        request.session['last_order_id'] = obj.id
        return redirect(payment)
    return redirect(Check_out_page)


def payment(request):
    data = PerfumeDB.objects.all()
    categories = PerfumeDB.objects.all()
    feature = PerfumeDB.objects.all()[:1]
    cart_total = 0
    pay_str = "0"
    payment = None
    uname = request.session.get('Username')
    if uname:
        cart_total = CartDb.objects.filter(Username=uname).count()
        customer = OrderDB.objects.filter(id=request.session.get('last_order_id')).first()
        pay = customer.Total_price if customer and customer.Total_price else 0
        amount = int(pay) * 100
        pay_str = str(amount)

        if amount > 0:
            import razorpay

            client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
            payment = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1",
            })
    return render(request, 'payment.html', {
        'data': data,
        "categories": categories,
        'feature': feature,
        'cart_total': cart_total,
        'pay_str': pay_str,
        'payment': payment,
    })
def end_page(request):
    feature = PerfumeDB.objects.filter()
    return render(request,'Thank.html',{'feature':feature})



