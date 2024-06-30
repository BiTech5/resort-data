from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('data/',views.add_data,name='data'),
   path('export-data/', views.export_data, name='export_data'),
   path('delete/<int:id>',views.delete,name='delete')
]
