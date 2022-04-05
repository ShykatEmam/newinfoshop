from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Brands, Feature
from .models import ShoppingMalls
import random


# for pagination 
from django.core.paginator import Paginator
# Create your views here.
# def index(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'Fast'
#     feature1.is_t = True
#     feature1.details = 'This is very fast'
#     features = [feature1]
#     for feature in features:
#         pass
#     return render(request,'index.html',{'features':features})

def index(request):
    mall_list = ShoppingMalls.objects.all().order_by('?')
    brand_list = Brands.objects.all().order_by('?')
    return render(request,'index.html',{'mall_lists':mall_list,'brands':brand_list})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if  User.objects.filter(email=email).exists():
                messages.info(request,'Email Already in use!!!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Exists!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1,2,3,4,5,'tim','tom','john']
    return render(request,'counter.html',{'posts': posts})

def post(request,pk):
    return render(request,'post.html',{'pk': pk})


def add_malls(request):
    if  request.method == 'POST':
        shopping_mall_name = request.POST['mall_name']
        category_1 = request.POST['product1']
        category_2 = request.POST['product2']
        category_3 = request.POST['product3']
        category_4 = request.POST['product4']
        category_5 = request.POST['product5']
        category_6 = request.POST['product6']
        category_7 = request.POST['product7']
        # here gmail = link1 = request.POST['link3']
        link1 = request.POST['link3']
        # website_link
        link2 = request.POST['link1']
        # facebook_link
        link3 = request.POST['link2']
        # other link
        link4 = request.POST['link4']
        # area = division
        division = request.POST['division']
        # address = location
        location = request.POST['location']
        
        phone_1 = request.POST['phone1']
        phone_2 = request.POST['phone2']
        phone_3 = request.POST['phone3']
        phone_4 = request.POST['phone4']
        
        image_0 = request.POST['image_0']
        image_1 = request.POST['image_1']
        image_2 = request.POST['image_2']
        image_3 = request.POST['image_3']
        image_4 = request.POST['image_4']
        # description = mall_description
        mall_description = request.POST['mall_description']
        
        facilities_1 = request.POST['facilities_1']
        facilities_2 = request.POST['facilities_2']
        facilities_3 = request.POST['facilities_3']
        facilities_4 = request.POST['facilities_4']
        facilities_5 = request.POST['facilities_5']
        facilities_6 = request.POST['facilities_6']
        facilities_7 = request.POST['facilities_7']
        facilities_8 = request.POST['facilities_8']
        facilities_9 = request.POST['facilities_9']
        facilities_10 = request.POST['facilities_10']
        facilities_11 = request.POST['facilities_11']
        facilities_12 = request.POST['facilities_12']
        facilities_13 = request.POST['facilities_13']
        facilities_14 = request.POST['facilities_14']
        facilities_15 = request.POST['facilities_15']
        
        floors_1 = request.POST['floors_1']
        floors_2 = request.POST['floors_2']
        floors_3 = request.POST['floors_3']
        floors_4 = request.POST['floors_4']
        floors_5 = request.POST['floors_5']
        floors_6 = request.POST['floors_6']
        floors_7 = request.POST['floors_7']
        floors_8 = request.POST['floors_8']
        floors_9 = request.POST['floors_9']
        floors_10 = request.POST['floors_10']
        floors_11 = request.POST['floors_11']
        floors_12 = request.POST['floors_12']

        shoppingMalls = ShoppingMalls.objects.create(shopping_mall_name =shopping_mall_name,description=mall_description,address=location,category_1=category_1,category_2=category_2,category_3=category_3,category_4=category_4,category_5=category_5,category_6=category_6,category_7=category_7,gmail_link=link1,website_link=link2,facebook_link=link3,other_link=link4,phone_1=phone_1,phone_2=phone_2,phone_3=phone_3,phone_4=phone_4,facilities_1=facilities_1,facilities_2=facilities_2,facilities_3=facilities_3,facilities_4=facilities_4,facilities_5=facilities_5,facilities_6=facilities_6,facilities_7=facilities_7,facilities_8=facilities_8,facilities_9=facilities_9,facilities_10=facilities_10,facilities_11=facilities_11,facilities_12=facilities_12,facilities_13=facilities_13,facilities_14=facilities_14,facilities_15=facilities_15,floors_1=floors_1,floors_2=floors_2,floors_3=floors_3,floors_4=floors_4,floors_5=floors_5,floors_6=floors_6,floors_7=floors_7,floors_8=floors_8,floors_9=floors_9,floors_10=floors_10,floors_11=floors_11,floors_12=floors_12,division=division,image_0=image_0,image_1=image_1,image_2=image_2,image_3=image_3,image_4=image_4)
        shoppingMalls.save();
        messages.info(request,'Mall Successfully Added')
        return render(request,'add_malls.html')
    else:
        messages.info(request,'Add correct data!!!')
        return render(request,'add_malls.html')

def malls(request):
    page_name = "Shopping Malls"
    p = Paginator(ShoppingMalls.objects.all(),5)
    page = request.GET.get('page')
    mall_paginators = p.get_page(page)
    return render(request,'malls.html',{'site_name': page_name,'mall_paginators':mall_paginators})

def brands(request):
    brand_name = "Brands"
    p = Paginator(Brands.objects.all(),5)
    page = request.GET.get('page')
    brand_paginators = p.get_page(page)
    shops = list(ShoppingMalls.objects.all())
    shops = random.sample(shops,5)
    return render(request,'brands.html',{'site_name': brand_name,'brand_paginators':brand_paginators,'shops':shops})

def about(request):
    return render(request,'about.html')

def brand_details(request):
    
    if  request.method == 'POST':
        page_title = request.POST['brand_title']




    pk = Brands.objects.all()
    items = list(Brands.objects.all())
    pks = random.sample(items,5)
    pks2 = random.sample(items,6)

    sp = ShoppingMalls.objects.all()
    spitems = list(ShoppingMalls.objects.all())
    sps = random.sample(spitems,5)
    sps2 = random.sample(spitems,6)



    return render(request,'brand_details.html',{'pk':pk,'page_title':page_title,'pks':pks,'sp':sp,'sps':sps,'sps2':sps2,'pks2':pks2})

def shop_details(request):
    if  request.method == 'POST':
        page_title = request.POST['mall_title']
    pk = Brands.objects.all()
    items = list(Brands.objects.all())
    pks = random.sample(items,5)
    return render(request,'mall_details.html')

def add_brands(request):
    if  request.method == 'POST':
        brand_name = request.POST['brand_name']
        # description = mall_description
        description = request.POST['description']

        category_1 = request.POST['category_1']
        category_2 = request.POST['category_2']
        category_3 = request.POST['category_3']
        category_4 = request.POST['category_4']
        category_5 = request.POST['category_5']
        category_6 = request.POST['category_6']
        category_7 = request.POST['category_7']
        # here gmail = link1 = request.POST['link3']
        link1 = request.POST['link3']
        # website_link
        link2 = request.POST['link1']
        # facebook_link
        link3 = request.POST['link2']
        # other link
        link4 = request.POST['link4']

        showrooms_1 = request.POST['showrooms_1']
        showrooms_2 = request.POST['showrooms_2']
        showrooms_3 = request.POST['showrooms_3']
        showrooms_4 = request.POST['showrooms_4']
        showrooms_5 = request.POST['showrooms_5']
        showrooms_6 = request.POST['showrooms_6']
        showrooms_7 = request.POST['showrooms_7']
        showrooms_8 = request.POST['showrooms_8']
        showrooms_9 = request.POST['showrooms_9']
        showrooms_10 = request.POST['showrooms_10']
        showrooms_11 = request.POST['showrooms_11']
        showrooms_12 = request.POST['showrooms_12']
        showrooms_13 = request.POST['showrooms_13']
        showrooms_14 = request.POST['showrooms_14']
        showrooms_15 = request.POST['showrooms_15']
        showrooms_16 = request.POST['showrooms_16']
        showrooms_17 = request.POST['showrooms_17']
        showrooms_18 = request.POST['showrooms_18']
        showrooms_19 = request.POST['showrooms_19']
        showrooms_phone_1 = request.POST['showrooms_phone_1']
        showrooms_phone_2 = request.POST['showrooms_phone_2']
        showrooms_phone_3 = request.POST['showrooms_phone_3']
        showrooms_phone_4 = request.POST['showrooms_phone_4']
        showrooms_phone_5 = request.POST['showrooms_phone_5']
        showrooms_phone_6 = request.POST['showrooms_phone_6']
        showrooms_phone_7 = request.POST['showrooms_phone_7']
        showrooms_phone_8 = request.POST['showrooms_phone_8']
        showrooms_phone_9 = request.POST['showrooms_phone_9']
        showrooms_phone_10 = request.POST['showrooms_phone_10']
        showrooms_phone_11 = request.POST['showrooms_phone_11']
        showrooms_phone_12 = request.POST['showrooms_phone_12']
        showrooms_phone_13 = request.POST['showrooms_phone_13']
        showrooms_phone_14 = request.POST['showrooms_phone_14']
        showrooms_phone_15 = request.POST['showrooms_phone_15']
        showrooms_phone_16 = request.POST['showrooms_phone_16']
        showrooms_phone_17 = request.POST['showrooms_phone_17']
        showrooms_phone_18 = request.POST['showrooms_phone_18']
        showrooms_phone_19 = request.POST['showrooms_phone_19']

        image_0 = request.POST['image_0']
        image_1 = request.POST['image_1']
        image_2 = request.POST['image_2']
        image_3 = request.POST['image_3']
        image_4 = request.POST['image_4']
        newbrand = Brands.objects.create(brand_name=brand_name, description=description, category_1=category_1, category_2=category_2, category_3=category_3, category_4=category_4, category_5=category_5, category_6=category_6, category_7=category_7, gmail_link=link1, website_link=link2, facebook_link=link3, other_link=link4, showrooms_1=showrooms_1, showrooms_2=showrooms_2, showrooms_3=showrooms_3, showrooms_4=showrooms_4, showrooms_5=showrooms_5, showrooms_6=showrooms_6, showrooms_7=showrooms_7, showrooms_8=showrooms_8, showrooms_9=showrooms_9, showrooms_10=showrooms_10, showrooms_11=showrooms_11, showrooms_12=showrooms_12, showrooms_13=showrooms_13, showrooms_14=showrooms_14, showrooms_15=showrooms_15, showrooms_16=showrooms_16, showrooms_17=showrooms_17, showrooms_18=showrooms_18, showrooms_19=showrooms_19, showrooms_phone_1=showrooms_phone_1, showrooms_phone_2=showrooms_phone_2, showrooms_phone_3=showrooms_phone_3, showrooms_phone_4=showrooms_phone_4, showrooms_phone_5=showrooms_phone_5, showrooms_phone_6=showrooms_phone_6, showrooms_phone_7=showrooms_phone_7, showrooms_phone_8=showrooms_phone_8, showrooms_phone_9=showrooms_phone_9, showrooms_phone_10=showrooms_phone_10, showrooms_phone_11=showrooms_phone_11, showrooms_phone_12=showrooms_phone_12, showrooms_phone_13=showrooms_phone_13, showrooms_phone_14=showrooms_phone_14, showrooms_phone_15=showrooms_phone_15, showrooms_phone_16=showrooms_phone_16, showrooms_phone_17=showrooms_phone_17, showrooms_phone_18=showrooms_phone_18, showrooms_phone_19=showrooms_phone_19, image_0=image_0, image_1=image_1, image_2=image_2, image_3=image_3, image_4=image_4)
        newbrand.save();
        messages.info(request,'Brand Successfully Added')
        return render(request,'add_brands.html')
    else:
        messages.info(request,'Add correct data!!!')
        return render(request,'add_brands.html')
