from django.db import models

# Create your models here.
class Company(models.Model):
    """ Company Model """
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    gst_number = models.CharField(max_length=30, blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class FoodPackage(models.Model):
    """ FoodPackage Model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    package_option = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.package_option


class Customer(models.Model):
    """ Customer Model """
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.customer_name


class CustomerAddress(models.Model):
    """ Customer Address Model"""
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.customer_id.customer_name


class Order(models.Model):
    """ Order Model """
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_cost = models.FloatField()
    discount = models.FloatField()
    final_cost = models.FloatField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.customer_id.name


class Orderdetails(models.Model):
    """ Order Details Model """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    foodpackage_id = models.ForeignKey(FoodPackage, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField()


class FortuneCookie(models.Model):
    """ FortuneCookie Model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    fortune_option = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.fortune_option