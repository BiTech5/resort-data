from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from import_export import resources
# Register your models here.
class CustomerAdmin(resources.ModelResource):
    class Meta:
        model= CustomerModel
admin.site.register(CustomerModel,ImportExportModelAdmin)