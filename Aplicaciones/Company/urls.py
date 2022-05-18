from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('createCompany/', views.createCompany),
    path('edicionCompany/<nit>', views.edicionCompany),
    path('editCompany/', views.editCompany),
    path('deleteCompany/<nit>', views.deleteCompany),
]
