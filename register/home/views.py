from django.shortcuts import render, redirect
from .models import Person
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        number=request.POST['number']
        password=make_password(request.POST['pwd'])
        user=Person.objects.create(name=name,Email=email,address=address,number=number,password=password)
        user.save()
        return render (request,'app/login.html')
        
        
    return render(request,'app/index.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if Person.objects.filter(Email=email).exists():
            obj=Person.objects.get(Email=email)
            password=obj.password
            
            if check_password(password, password):
                return redirect('/showdata/')
            else:
                messages.error(request,'password incorrect')
                return redirect('/')
        else:
            messages.error(request, 'password incorrect')
    else:
        return redirect('/')
    return render(request,'app/login.html') 
def update(request, uid):
    res = Person.objects.get(id=uid)
    return render(request, 'app/update.html', context={

        'person': res,
    })
    
# def updatedata(request):
#     if request.method=='POST':
#         uid=request.POST['uid']
#         name=request.POST['name']
#         email=request.POST['email']
#         address=request.POST['address']
#         number=request.POST['number']
#         user=Person.objects.filter(id=uid).update(name=name,email=email,address=address,number=number)
#         return redirect('/showdata')
 
def updatedata(request):
    id=request.POST['uid']
    user=Person.objects.get(id=id)
    user.name=request.POST['name']
    user.Email=request.POST['email']
    user.address=request.POST['address']
    user.number=request.POST['Phone']
    user.save()
    data=Person.objects.all()
    return render (request,'app/showdata.html',{'data':data})
        
def showdata(request):
    data=Person.objects.all()
    return render(request,'app/showdata.html',{'data':data})
    
    
def signin(request):
    return render(request,'app/login.html')

def delete(request):
    id=request.GET['id']
    Person.objects.get(id=id).delete()
    data=Person.objects.all()
    return render(request,'app/showdata.html',{'data':data})
    