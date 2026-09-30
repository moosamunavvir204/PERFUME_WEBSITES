from urllib.request import Request

from django.contrib.admin import display
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.template.context_processors import request
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from  django.contrib import messages


from Adminapp.models import *
# Create your views here.
def dashboard(request):
    return render(request,'Dashboard.html')
def add_page(request):
    categories = PerfumeDB.objects.all()
    perfume = PerfumeDB.objects.all()
    return render(request, 'add_perfume.html',{'perfume':perfume,'categories':categories})
def save_perfume(request):
    if request.method =="POST":
        category = request.POST.get("category")
        description= request.POST.get("description")
        img = request.FILES["image"]
        obj=PerfumeDB(category=category,description=description,perfume_Image=img)
        obj.save()
        messages.success(request,'Perfumes Added Successfully')
        return redirect(add_page)
def details_page(request):
    data = PerfumeDB.objects.all()
    return render(request, 'perfume_details.html',{'data': data})


def edit_page(request, per_id):
    data = PerfumeDB.objects.get(id=per_id)
    return render(request, 'Edit.html', {'data': data})
def Update_Perfume(request,per_id):
    if request.method =="POST":
        category = request.POST.get("category")
        description = request.POST.get("description")
        try:
            img = request.FILES["image"]
            obj = FileSystemStorage()
            file = obj.save(img.name, img)
        except MultiValueDictKeyError:
            file = PerfumeDB.objects.get(id=per_id).perfume_Image
        PerfumeDB.objects.filter(id=per_id).update(category=category,description=description,perfume_Image=file)
        return redirect(details_page)


def delete_page(request,per_id):
    data = PerfumeDB.objects.filter(id=per_id)
    data.delete()
    return redirect(details_page)


def product_page(request):
    categories = PerfumeDB.objects.all()
    return render(request,'add_product.html',{'categories':categories})
def save_product(request):
    if request.method =="POST":
        product_name = request.POST.get("product_name")
        brand= request.POST.get("brand")
        category_name = request.POST.get("category_name")
        size = request.POST.get("size")
        price = request.POST.get("price")
        description = request.POST.get("description")
        img = request.FILES["image"]
        obj=ProductDB(product_name=product_name,brand=brand,category_name=category_name,size=size,price=price,description=description,product_Image=img)
        obj.save()
        messages.success(request,'product Added Successfully')
        return redirect(add_page)
def product_details(request):
    product = ProductDB.objects.all()
    return render(request,'product_details.html',{"product":product})
def edit_product(request, pro_id):
    products = ProductDB.objects.get(id=pro_id)
    return render(request, 'Edit_product.html', {'products': products})
def Update_Product(request,pro_id):
    if request.method =="POST":
        product_name = request.POST.get("product_name")
        brand = request.POST.get("brand")
        category_name = request.POST.get("category_name")
        size = request.POST.get("size")
        price = request.POST.get("price")
        description = request.POST.get("description")
        try:
            img = request.FILES["image"]
            obj = FileSystemStorage()
            file = obj.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=pro_id).product_Image
        ProductDB.objects.filter(id=pro_id).update(product_name=product_name,brand=brand,category_name=category_name,size=size,price=price,description=description,product_Image=file)
        return redirect(product_details)
def delete_product(request,pro_id):
    products = ProductDB.objects.filter(id=pro_id)
    products.delete()
    return redirect(product_details)

def Client_page(request):
    return render(request,'Client.html')
def Client_details(request):
    client = ClientDB.objects.all()
    return render(request,'Client_details.html',{"client":client})
def save_Client(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    img = request.FILES["image"]
    obj = ClientDB(name=name, description=description, Client_Image=img)
    obj.save()
    messages.success(request, 'client Added Successfully')
    return redirect(Client_page)
def edit_client(request,clint_id ):
    client = ClientDB.objects.get(id=clint_id)
    return render(request, 'edit_lient.html', {'client': client})
def Update_Client(request,clint_id):
    name = request.POST.get("name")
    description = request.POST.get("description")
    try:
        img = request.FILES["image"]
        obj = FileSystemStorage()
        file = obj.save(img.name, img)
    except MultiValueDictKeyError:
        file = ClientDB.objects.get(id=clint_id).Client_Image
    ClientDB.objects.filter(id=clint_id).update(name=name, description=description, Client_Image=file)
    return redirect(Client_details)
def delete_client(request,clint_id):
    client = ClientDB.objects.filter(id=clint_id)
    client.delete()
    return redirect(Client_details)
def banner_page(request):
    return render(request,'banner.html')
def banner_details(request):
    banner =BannerDB.objects.all()
    return render(request,'banner_details.html',{'banner':banner})
def save_banner(request):
    img = request.FILES["image"]
    obj = BannerDB( Banner_Video=img)
    obj.save()
    messages.success(request, 'banner Added Successfully')
    return redirect(banner_page)
def edit_banner(request,banner_id):
    banner = BannerDB.objects.get(id=banner_id)
    return render(request,'edit_banner.html',{'banner':banner})
def update_banner(request,banner_id):
    try:
        img = request.FILES["image"]
        obj = FileSystemStorage()
        file = obj.save(img.name, img)
    except MultiValueDictKeyError:
        file = BannerDB.objects.get(id=banner_id).Banner_Video
    BannerDB.objects.filter(id=banner_id).update(Banner_Video=file)
    return redirect(banner_details)
def delete_banner(request,banner_id):
    banner = ClientDB.objects.filter(id=banner_id)
    banner.delete()
    return redirect(banner_details)



