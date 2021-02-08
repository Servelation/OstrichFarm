import self as self
from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.actions import delete_selected
from django.core.management import call_command
from django.core.management import execute_from_command_line
from django.shortcuts import redirect
from reversion.admin import VersionAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
from .models import *
import os
from adminbuttons.django_admin_buttons import ButtonAdmin
# class ClientResource(resources.ModelResource):
#     class Meta:
#         model = Client

@admin.register(Client)
class ClientAdmin(VersionAdmin):
    list_display = ('id', 'Surname', 'Name', 'Patronymic', 'PhoneNumber', 'PassportSeries', 'PassportID')
    list_display_links = ('id', 'Surname', 'Name', 'Patronymic')
    search_fields = ('Surname', 'Name', 'Patronymic', 'PhoneNumber', 'PassportSeries', 'PassportID')


#VersionAdmin
@admin.register(Employee)
class EmployeeAdmin(VersionAdmin):
    list_display = ('id', 'Surname', 'Name', 'Patronymic', 'Age','Position','Salary','WarehouseID')
    list_display_links = ('id', 'Surname', 'Name', 'Patronymic')
    search_fields = ('id', 'Surname', 'Name', 'Patronymic', 'Age','Position','Salary','WarehouseID')
    # def get_urls(self):
    #     urls = super().get_urls()
    #     my_urls = [
    #         path('export/', self.export),
    #         path('import/',self.imp)
    #     ]
    #     return my_urls + urls

    def export(self, request):
        call_command('dbbackup')
        self.message_user(request, "Создан дамп базы данных")
        return HttpResponseRedirect("../")

    def imp(self,request):
        call_command('dbrestore')
        self.message_user(request, "База данных восстановлена")
        return HttpResponseRedirect("../")


@admin.register(Product)
class ProductAdmin(VersionAdmin):
    list_display = ('id', 'Kind', 'Price', 'Count','WarehousId')
    list_display_links = ('id', 'Kind', 'Price', 'Count')
    search_fields = ('id', 'Kind', 'Price', 'Count','WarehousId')

@admin.register(OrderProducts)
class OrderProductsAdmin(VersionAdmin):
    list_display = ('id', 'Price', 'Cost', 'Count', 'OrderID', 'ProductID')
    list_display_links = ('id', 'Price', 'Count')
    search_fields =('id', 'Price', 'Cost', 'Count', 'OrderID', 'ProductID')

@admin.register(Order)
class OrderAdmin(VersionAdmin):
    list_display = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status','ClientId','EmployeeID')
    list_display_links = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status')
    search_fields = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status','ClientId','EmployeeID')

@admin.register(Ostrich)
class OstrichAdmin(VersionAdmin):
    list_display = ('id', 'Nickname', 'Sex', 'HealthStatus', 'PaddockID','VaccinationID')
    list_display_links = ('id', 'Nickname', 'Sex', 'HealthStatus', 'PaddockID','VaccinationID')
    search_fields = ('id', 'Nickname', 'Sex', 'HealthStatus', 'PaddockID','VaccinationID')

@admin.register(Paddock)
class PaddockAdmin(VersionAdmin):
    list_display = ('id', 'Address', 'NumberOfPlaces', 'Area', 'PriceOfRent')
    list_display_links = ('id', 'Address', 'NumberOfPlaces', 'Area', 'PriceOfRent')
    search_fields = ('id', 'Address', 'NumberOfPlaces', 'Area', 'PriceOfRent')

@admin.register(Provider)
class ProviderAdmin(VersionAdmin):
    list_display = ('id', 'Surname', 'Name', 'Patronymic', 'PhoneNumber')
    list_display_links = ('id', 'Surname', 'Name', 'Patronymic', 'PhoneNumber')
    search_fields = ('id', 'Surname', 'Name', 'Patronymic', 'PhoneNumber')

@admin.register(RawMaterial)
class RawMaterialAdmin(VersionAdmin):
    list_display = ('id', 'Kind', 'Price', 'Count','WarehousId')
    list_display_links = ('id', 'Kind', 'Price', 'Count','WarehousId')
    search_fields = ('id', 'Kind', 'Price', 'Count','WarehousId')

@admin.register(Supply)
class SupplyAdmin(VersionAdmin):
    list_display = ('id','DateOfSupply' ,'Price', 'Cost', 'Count', 'RawMaterialID')
    list_display_links = ('id','DateOfSupply' ,'Price', 'Cost', 'Count')
    search_fields =('id','DateOfSupply' ,'Price', 'Cost', 'Count', 'RawMaterialID', 'ProviderID ')

@admin.register(Vaccination)
class VaccinationAdmin(VersionAdmin):
    list_display = ('id','ApplicationDate' )
    list_display_links = ('id','ApplicationDate' )
    search_fields =('id','ApplicationDate' )

@admin.register(Vaccine)
class VaccineAdmin(VersionAdmin):
    list_display = ('id','Name','Diseade', 'Validity','VaccinationID')
    list_display_links = ('id','Name','Diseade', 'Validity','VaccinationID')
    search_fields =('id','Name','Diseade', 'Validity','VaccinationID')

@admin.register(Warehouse)
class WarehouseAdmin(VersionAdmin):
    list_display = ('id','Address','Name')
    list_display_links = ('id','Address','Name')
    search_fields =('id','Address','Name')
# admin.site.register(Client, ClientAdmin)
#admin.site.register(Employee,EmployeeAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderProducts, OrderProductsAdmin)
# admin.site.register(Ostrich)
# admin.site.register(Paddock)
# admin.site.register(Product,ProductAdmin)
# admin.site.register(Provider)
# admin.site.register(RawMaterial)
# admin.site.register(Supply)
# admin.site.register(Vaccination)
# admin.site.register(Vaccine)
# admin.site.register(Warehouse)


