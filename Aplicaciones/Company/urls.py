from django.urls import path

from . import views

 # //todaas las urls de la aplicacion
urlpatterns = [
    path('companies', views.home, name='home'),
    path('companies/<nit>', views.nitCompany, name='nitCompany'),
    path('companies/create', views.createCompany),
    path('companies/edit/<nit>', views.editCompany),
    path('companies/delete/<nit>', views.deleteCompany),
]
