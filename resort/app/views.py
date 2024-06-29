from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    data=CustomerModel.objects.all()
    return render(request,'index.html',{'data':data})


def add_data(request):
    return render(request,'form.html')