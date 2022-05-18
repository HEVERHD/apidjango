from operator import index
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Company

# Create your views here.


def home(request):
    listCompanyes = Company.objects.all()
    return JsonResponse(listCompanyes, safe=False)
    



def createCompany(request):
    nit = request.POST['numNit']
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    address = request.POST['txtAddress']
    phone = request.POST['numPhone']

    company = Company.objects.create(
        nit=nit, name=name, description=description, address=address, phone=phone)
    return redirect('/')


def edicionCompany(request, nit):
    company = Company.objects.get(nit=nit)
    return render(request, "edicionCompany.html", {'company': company})


def editCompany(request):
    nit = request.POST['numNit']
    name = request.POST['txtName']
    description = request.POST['txtDescription']
    address = request.POST['txtAddress']
    phone = request.POST['numPhone']

    company = Company.objects.get(nit=nit)
    company.nit = nit
    company.name = name
    company.description = description
    company.address = address
    company.phone = phone
    company.save()
    return redirect('/')


def deleteCompany(request, nit):
    company = Company.objects.get(nit=nit)
    company.delete()
    return redirect('/')
