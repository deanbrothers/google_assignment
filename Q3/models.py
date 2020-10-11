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

class CarpetType(models.Model):
    """ Carpet Category Model """
    carpet_type = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.carpet_type

class Carpet(models.Model):
    """ Carpet  Model """
    name = models.CharField(max_length=30)
    carpet_type = models.ForeignKey(CarpetType, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    available_carpet = models.FloatField()
    colour = models.CharField(max_length=30)
    in_stock = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class CarpetRoll(models.Model):
    """ Carpet Roll Model """
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)
    roll_r1_width = models.FloatField()
    roll_r1_length = models.FloatField()
    roll_r2_width = models.FloatField()
    roll_r2_length = models.FloatField()
    available_area = models.FloatField()
    added_date = models.DateField()
    updated_date = models.DateField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class CarpetInventory(models.Model):
    """ Carpet  Inventory Model """
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)
    available_roll_count = models.IntegerField()
    sold_roll_count = models.IntegerField()
    total_roll_count = models.IntegerField()
    def __str__(self):
        return str(self.roll_count)

class PurchaseOrder(models.Model):
    """ Purchase Order Model """
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    order_cost = models.FloatField()
    status = models.BooleanField(default=True)


class PurchaseOrderCarpet(models.Model):
    """ Carpets details for purchase order """
    carpet = models.ForeignKey(Carpet, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    carpet_width = models.FloatField()
    carpet_length = models.FloatField()
    carpet_cost = models.FloatField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.carpet.name


class Customer(models.Model):
    """ Customer Model """
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.customer_name

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
    """ Order details Model """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    roll_id = models.ForeignKey(CarpetRoll, on_delete=models.CASCADE)
    carpet_id = models.ForeignKey(Carpet, on_delete=models.CASCADE)
    carpet_width = models.FloatField()
    carpet_length = models.FloatField()
    mrp = models.FloatField()
    discount = models.FloatField()
    price = models.FloatField()
    status = models.BooleanField(default=True)
