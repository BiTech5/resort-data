from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    data=CustomerModel.objects.all()
    return render(request,'index.html',{'data':data})


def add_data(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        arrival=request.POST.get('arrival')
        departure=request.POST.get('departure')
        pax=request.POST.get('pax')
        stay=request.POST.get('stay_type')
        package=request.POST.get('package')
        tariff=request.POST.get('tariff')
        advance=request.POST.get('advance')
        remark=request.POST.get('remark')
        print(name)
    return render(request,'form.html')