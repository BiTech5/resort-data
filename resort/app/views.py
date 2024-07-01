from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .admin import *
from django.views.generic import ListView , FormView
from django.db.models import Q
# Create your views here.
def home(request):
    data=CustomerModel.objects.all()
    query=request.POST.get('search','')
    result=CustomerModel.objects.filter(
        Q(name__icontains=query) |
        Q(contact__icontains=query) |
        Q(arrivals__icontains=query) |
        Q(stay_type__icontains=query)
    )
    if result:
        return render(request,'index.html',{'data':result})
    else:
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
        remark=request.POST.get('remarks')
        #instance for model data
        
        customer=CustomerModel(name=name,
                               contact=contact,
                               arrivals=arrival,
                               departure=departure,
                               pax=pax,
                               stay_type=stay,
                               package=package,
                               tariff=tariff,
                               advance=advance,
                               remarks=remark)
        customer.save()
        return redirect('home')
        
    return render(request,'form.html')

def delete(request, id):
    dele=CustomerModel.objects.get(id=id)
    dele.delete()
    return redirect('home')
def export_data(request):
    resource = CustomerAdmin()
    dataset = resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="customer_data.xlsx"'
    return response
def update(request,id):
    data=get_object_or_404(CustomerModel, id=id)
    
    if request.method=='POST':
        data.name=request.POST.get('name')
        data.contact=(request.POST.get('contact'))
        data.arrivals=request.POST.get('arrival')
        data.departure=request.POST.get('departure')
        data.pax=request.POST.get('pax')
        data.stay_type=request.POST.get('stay_type')
        data.package=request.POST.get('package')
        data.tariff=request.POST.get('tariff')
        data.advance=request.POST.get('advance')
        data.remarks=request.POST.get('remarks')
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})