from django.urls import path

from . import views

urlpatterns = [
    path('companies', views.home, name='home'),
    path('companies/create', views.createCompany),
    path('companies/edit/<nit>', views.editCompany),
    path('companies/delete/<nit>', views.deleteCompany),
]
