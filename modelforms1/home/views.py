from django.shortcuts import render
from .forms import EmpForm
from.models import Emp
from django.db.models import Max,Min,Avg,Sum
def index(request):
    e=EmpForm()
    mx=Emp.objects.aggregate(Max('sal'))
    mn=Emp.objects.aggregate(Min('sal'))
    ag=Emp.objects.aggregate(Avg('sal'))
    sm=Emp.objects.aggregate(Sum('sal'))
    return render(request,'index.html',{'e':e,'mx':mx,'mn':mn,'ag':ag,'sm':sm})
def addimage(request):
    e=EmpForm(request.POST,request.FILES)
    if e.is_valid():
        e.save()
    else:
        print('invalid data')
    data=Emp.objects.all()
    return render(request,'show.html',{'data':data})        