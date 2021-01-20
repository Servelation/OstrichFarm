from django.contrib import admin

# Register your models here.
from .models import *
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Surname', 'Name', 'Patronymic', 'PhoneNumber', 'PassportSeries', 'PassportID')
    list_display_links = ('id', 'Surname', 'Name', 'Patronymic')
    search_fields = ('Surname', 'Name', 'Patronymic', 'PhoneNumber', 'PassportSeries', 'PassportID')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Surname', 'Name', 'Patronymic', 'Age','Position','Salary','WarehouseID')
    list_display_links = ('id', 'Surname', 'Name', 'Patronymic')
    search_fields = ('id', 'Surname', 'Name', 'Patronymic', 'Age','Position','Salary','WarehouseID')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'Kind', 'Price', 'DateOfReceiving', 'Count','WarehousId')
    list_display_links = ('id', 'Kind', 'Price', 'DateOfReceiving', 'Count')
    search_fields = ('id', 'Kind', 'Price', 'DateOfReceiving', 'Count','WarehousId')

class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Price', 'Cost', 'Count', 'OrderID', 'ProductID')
    list_display_links = ('id', 'Price', 'Count')
    search_fields =('id', 'Price', 'Cost', 'Count', 'OrderID', 'ProductID')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status','ClientId','EmployeeID')
    list_display_links = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status')
    search_fields = ('id', 'Cost', 'DateOfRegistration', 'DateOfCompletion', 'Status','ClientId','EmployeeID')
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProducts, OrderProductsAdmin)
admin.site.register(Ostrich)
admin.site.register(Paddock)
admin.site.register(Product,ProductAdmin)
admin.site.register(Provider)
admin.site.register(RawMaterial)
admin.site.register(Supply)
admin.site.register(Vaccination)
admin.site.register(Vaccine)
admin.site.register(Warehouse)