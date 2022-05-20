import json
from operator import index
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Company
from django.forms.models import model_to_dict

# Create your views here.


def home(request):
    listCompanyes = list(Company.objects.values())
    return JsonResponse(listCompanyes, safe=False)


def nitCompany(request, nit):
    nitCompany = Company.objects.get(nit=nit)
    return JsonResponse(model_to_dict(nitCompany), safe=False)

def createCompany(request):
    json_data = json.loads(request.body)

    nit = json_data['nit']
    name = json_data['name']
    description = json_data['description']
    address = json_data['address']
    phone = json_data['phone']

    company = Company.objects.create(
        nit=nit, name=name, description=description, address=address, phone=phone)
    return JsonResponse(json_data, safe=False)


def edicionCompany(request, nit):
    company = Company.objects.get(nit=nit)
    return render(request, "edicionCompany.html", {'company': company})


def editCompany(request, nit):
    json_data = json.loads(request.body)

    nitnew = json_data['nit']
    name = json_data['name']
    description = json_data['description']
    address = json_data['address']
    phone = json_data['phone']

    company = Company.objects.get(nit=nit)
    company.nit = nitnew
    company.name = name
    company.description = description
    company.address = address
    company.phone = phone
    company.save()
    return JsonResponse(json_data, safe=False)


def deleteCompany(request, nit):
    company = Company.objects.get(nit=nit)
    company.delete()
    return JsonResponse({}, safe=False)
