from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

User = get_user_model()

# Create your models here.
class Client(models.Model):
    Surname = models.CharField(max_length=64, verbose_name='Фамилия')
    Name = models.CharField(max_length=64, verbose_name='Имя')
    Patronymic = models.CharField(max_length=64, verbose_name='Отчество')
    PassportSeries = models.IntegerField(blank=True, default=0, verbose_name='Серия паспорта')
    PassportID = models.IntegerField(blank=True, default=0, verbose_name='Номер паспорта')
    PhoneNumber = models.IntegerField(blank=True, default=0, verbose_name='Номер телефона')

    def __str__(self):
        return str(self.pk)+"  "+self.Surname+" "+self.Name+" "+self.Patronymic+"  +"+str(self.PhoneNumber)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['Surname']


class Employee(models.Model):
    Name = models.CharField(max_length=64, verbose_name='Имя')
    Surname = models.CharField(max_length=64, verbose_name='Фамилия')
    Patronymic = models.CharField(max_length=64, verbose_name='Отчество')
    PhoneNumber = models.IntegerField(blank=True, default=0, verbose_name='Телефонный номер')
    Age = models.IntegerField(blank=True, default=0, verbose_name='Возраст')
    Position = models.CharField(max_length=64, verbose_name='Должность')
    Salary = models.IntegerField(blank=True, default=0, verbose_name='Зарплата')
    WarehouseID =models.ForeignKey('Warehouse', on_delete=models.PROTECT, null=True, verbose_name='Склад')

    def __str__(self):
        return str(self.pk) + "  " + self.Surname + " " + self.Name + " " + self.Patronymic + "  +" + str(self.PhoneNumber)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['Surname']

class Order(models.Model):
    Cost = models.FloatField( default=0, verbose_name='Cтоимость')
    DateOfRegistration = models.DateTimeField(blank=True,null=True, verbose_name='Дата регистрации')
    DateOfCompletion = models.DateTimeField(blank=True,null=True, verbose_name='Дата завершения')
    Status = models.CharField(max_length=64, verbose_name='Статус')
    ClientId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Клиент')
    EmployeeID= models.ForeignKey('Employee',blank=True, on_delete=models.CASCADE, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return str(self.pk)+ "  " + str(self.DateOfRegistration)+ "  " + str(self.Status) + "  " + str(self.DateOfCompletion)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['DateOfRegistration']


class OrderProducts(models.Model):
    Kind = models.CharField(max_length=64  , verbose_name='Тип', default='Перья')
    Price = models.FloatField( default=0, verbose_name='Цена')
    Cost = models.FloatField( default=0, verbose_name='Стоимость')
    Count = models.IntegerField( default=0, verbose_name='Количество')
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, verbose_name='Заказ')
    ProductID = models.ForeignKey('Product', on_delete=models.PROTECT, null=True, verbose_name='Товар')

    def __str__(self):
        return str(self.pk)+ "  "+str(self.Price)+ "  "+str(self.Count)+ "  "+str(self.Cost)

    class Meta:
        verbose_name = 'Заказ продукта'
        verbose_name_plural = 'Заказы продуктов'
        ordering = ['OrderID']

class Ostrich(models.Model):
    Nickname = models.CharField(max_length=64, verbose_name='Кличка')
    Sex = models.CharField(max_length=64, verbose_name='Пол')
    HealthStatus=models.CharField(max_length=32, verbose_name='Статус здоровья')
    PaddockID = models.ForeignKey('Paddock', on_delete=models.PROTECT, null=True, verbose_name='Загон')
    VaccinationID = models.ForeignKey('Vaccination', on_delete=models.PROTECT, null=True, verbose_name='Вакцинация')
    def __str__(self):
        return str(self.pk)+ "  "+str(self.Nickname)+ "  "+str(self.Sex)+ "  "+str(self.HealthStatus)

    class Meta:
        verbose_name = 'Страус'
        verbose_name_plural = 'Страусы'
        ordering = ['PaddockID']


class Paddock(models.Model):
    Address = models.CharField(max_length=64, blank=True, verbose_name='Адрес')
    NumberOfPlaces= models.IntegerField(blank=True, default=0, verbose_name='Количество мест')
    Area = models.FloatField(blank=True, default=0, verbose_name='Площадь')
    PriceOfRent = models.FloatField(blank=True, default=0, verbose_name='Цена аренды')

    def __str__(self):
        return str(self.pk)+ "  "+str(self.Address)+ "  "+str(self.NumberOfPlaces)+ "  "+str(self.Area)+ "  "+str(self.PriceOfRent)

    class Meta:
        verbose_name = 'Загон'
        verbose_name_plural = 'Загоны'
        ordering = ['Address']
class Product(models.Model):
    Kind = models.CharField(max_length=32, verbose_name='Тип')
    Price = models.FloatField(blank=True, default=0, verbose_name='Цена')
    Count = models.IntegerField(blank=True, default=0, verbose_name='Количество')
    WarehousId = models.ForeignKey('Warehouse', on_delete=models.PROTECT, null=True, verbose_name='Склад')

    def __str__(self):
        return str(self.pk)+ "  "+self.Kind+ "  "+str(self.Price)+ "  "+str(self.Count)+ "  "+str(self.Price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['Kind']


class Provider(models.Model):
    Name = models.CharField(max_length=64, verbose_name='Имя')
    Surname = models.CharField(max_length=64, verbose_name='Фамилия')
    Patronymic = models.CharField(max_length=64, verbose_name='Отчество')
    Address = models.CharField(max_length=64, verbose_name='Адрес')
    PhoneNumber = models.IntegerField(blank=True, default=0, verbose_name='Номер телефона')

    def __str__(self):
        return str(self.pk)+ "  "+self.Name+ "  "+self.Surname+ "  "+self.Patronymic+ "  "+self.Address+ "  "+str(self.PhoneNumber)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['Surname']
class RawMaterial(models.Model):
    Kind = models.CharField(max_length=32,verbose_name='Тип', unique=True)
    Price = models.FloatField(blank=True, default=0,verbose_name='Цена')
    Count = models.FloatField(blank=True, default=0,verbose_name='Количество')
    WarehousId = models.ForeignKey('Warehouse', on_delete=models.PROTECT, null=True,verbose_name='Склад')
    def __str__(self):
        return str(self.pk)+ "  "+self.Kind+ "  "+self.Kind+ "  "+str(self.Count)

    class Meta:
        verbose_name = 'Cырье'
        verbose_name_plural = 'Сырье'
        ordering = ['Price']
class Supply(models.Model):
    DateOfSupply = models.DateTimeField(auto_now = True,verbose_name='Дата поставки')
    Price = models.FloatField(blank=True, default=0,verbose_name='Цена')
    Count = models.FloatField(blank=True, default=0,verbose_name='Количество')
    Cost =  models.FloatField(blank=True, default=0,verbose_name='Стоимость')
    RawMaterialID = models.ForeignKey('RawMaterial', on_delete=models.PROTECT,null=True,verbose_name='Сырье')
    ProviderID = models.ForeignKey('Provider', on_delete=models.PROTECT,null=True,verbose_name='Поставщик')

    def __str__(self):
        return str(self.pk)+ "  "+str(self.DateOfSupply)+ "  "+ str(self.Price)+ "  "+ str(self.Count)+ "  "+ str(self.Cost)

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        ordering = ['Cost']

    def save(self, *args, **kwargs):
        raw = RawMaterial.objects.get(pk=self.RawMaterialID.pk)
        raw.Count += self.Count
        raw.save()
        super(Supply, self).save(*args, **kwargs)

class Vaccination(models.Model):
    ApplicationDate = models.DateField(auto_now_add= True,verbose_name='Дата')
    def __str__(self):
        return str(self.pk)+ "  "+str(self.ApplicationDate)

    class Meta:
        verbose_name = 'Вакцинация'
        verbose_name_plural = 'Вакцинации'
class Vaccine(models.Model):
    Name  = models.CharField(max_length=64,verbose_name='Наименование')
    Diseade = models.CharField(max_length=64,verbose_name='Болезнь')
    Validity = models.IntegerField(blank=True, default=0,verbose_name='Срок действия')
    VaccinationID =models.ForeignKey('Vaccination', on_delete=models.PROTECT, null=True,verbose_name='Вакцинация')
    def __str__(self):
        return str(self.pk)+ "  "+self.Name+ "  "+self.Diseade+ "  "+str(self.Validity)

    class Meta:
        verbose_name = 'Вакцина'
        verbose_name_plural = 'Вакцины'
        ordering = ['Diseade']
class Warehouse(models.Model):
    Address =models.CharField(max_length=128,verbose_name='Адрес')
    Name = models.CharField(max_length=64,verbose_name='Название')

    def __str__(self):
        return str(self.pk)+ "  "+self.Address+ "  "+ self.Name

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['Name']