from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import stationdetails
from .models import reviews
from json import dumps

# Create your views here.

def index(request):
    return render(request, "index.html")

def map(request):
    stationdetail =list(stationdetails.objects.all())
   
    dataset=[]
   
    for i in range(0,len(stationdetail)):
        print(stationdetail[i].name)
        dataDictionary = {
            'name': stationdetail[i].name,
            'latitude': stationdetail[i].latitude,
            'longitude': stationdetail[i].longitude,
            'chargeprice': stationdetail[i].chargeprice,
            'charger1': stationdetail[i].charger1,
            'charger2': stationdetail[i].charger2,
            'charger3': stationdetail[i].charger3,
            'charger4': stationdetail[i].charger4,
        }
        dataJSON = dumps(dataDictionary)
        dataset.append(dataDictionary)
    return render(request,'map.html',{'data': dumps(dataset)})

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            if User.objects.filter(username='cypher'):
                return redirect('addpoint')
            else:
                return redirect('index.html')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            if User.objects.filter(username='cypher'):
                return redirect('addpoint')
            else:
                return redirect('index.html')
        else:
            return render(request,"login.html")

def register(request):
    return render(request, "index.html")

def logout(request):
    auth_logout(request)
    return redirect('./')
    

def addpoint(request):
    if User.objects.filter(username='cypher'):
        stationdetail =list(stationdetails.objects.all())
        dataset=[]
        # dump data
    
        for i in range(0,len(stationdetail)):
            print(stationdetail[i].name)
            dataDictionary = {
                'name': stationdetail[i].name,
                'latitude': stationdetail[i].latitude,
                'longitude': stationdetail[i].longitude,
                'chargeprice': stationdetail[i].chargeprice,
                'charger1': stationdetail[i].charger1,
                'charger2': stationdetail[i].charger2,
                'charger3': stationdetail[i].charger3,
                'charger4': stationdetail[i].charger4
            }
            dataJSON = dumps(dataDictionary)
            dataset.append(dataDictionary)
        return render(request,'addpoint.html',{'data': dumps(dataset)})
    else:
        return render(request, 'login.html')
    
def details(request):
    return render(request,'details.html')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        price = request.POST.get('price')
        chargetype1 = request.POST.get('chargetype1')
        if chargetype1 != "AC Type1":
            chargetype1 = "Null"
        chargetype2 = request.POST.get('chargetype2')
        if chargetype2 != "CCS-1":
            chargetype2 = 'Null'
        chargetype3 = request.POST.get('chargetype3')
        if chargetype3 != "Tesla Charge":
            chargetype3 = 'Null'
        chargetype4 = request.POST.get('chargetype4')
        if chargetype4 != "AC Plug Point":
            chargetype4 = "Null"
        address = request.POST.get('address')
        en = stationdetails(name=name,latitude=latitude,longitude=longitude,chargeprice=price,charger1=chargetype1,charger2=chargetype2,charger3=chargetype3,charger4=chargetype4,address=address)
        en.save()
    else:
        pass
    return render(request, 'success.html')

def details(request, name):
    stationdetail =list(stationdetails.objects.filter(name=name).all())
    reviewset =list(reviews.objects.filter(stationname=name).all())
    dataset=[]
        # dump data
    for i in range(0,len(reviewset)):
        dataDictionary = {
            'username': reviewset[i].username,
            'highlights': reviewset[i].highlights,
            'rating': reviewset[i].rating,
            'description': reviewset[i].description
        }
        dataJSON = dumps(dataDictionary)
        dataset.append(dataDictionary)
        datasetmain = {
            "data": dataDictionary
        }

    return render(request,'details.html',{'data': dumps(dataset),'stationname':name, 'price':stationdetail[0].chargeprice, 'address':stationdetail[0].address, 'charger':[stationdetail[0].charger1, stationdetail[0].charger2 ,stationdetail[0].charger3,stationdetail[0].charger4]})

def addreviews(request, stationname):
    print(stationname)
    print('-------------------')
    print(request.POST.get('highlights'))
    if request.method == 'POST':
        username = request.POST.get('username')
        highlights = request.POST.get('highlights')
        rating = request.POST.get('myRange')
        description = request.POST.get('description')

        en = reviews(username=username,stationname=stationname,highlights=highlights,rating=rating,description=description)
        en.save()
    else:
        pass
    return render(request, 'success.html')