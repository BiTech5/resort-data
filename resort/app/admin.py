from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.
class CustomerAdmin(ImportExportActionModelAdmin):
    list_display=['name']
admin.site.register(CustomerModel,CustomerAdmin)