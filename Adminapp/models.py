from django.db import models

# Create your models here.


# Create your models here.
class PerfumeDB(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    perfume_Image = models.ImageField(upload_to="perfume profiles", null=True, blank=True)

# ------------------------------------------------------------------------------------------------------
class ProductDB(models.Model):
    product_name = models.CharField(max_length=100,null=True,blank=True)
    brand = models.CharField(max_length=100,null=True,blank=True)
    category_name = models.CharField(max_length=100,null=True,blank=True)
    size = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100, null=True, blank=True)
    product_Image = models.ImageField(upload_to="image profiles", null=True, blank=True)
    # ------------------------------------------------------------------------------------------------------
class BannerDB(models.Model):
    Banner_Image = models.ImageField(upload_to="Banner profiles", null=True, blank=True)
    # ------------------------------------------------------------------------------------------------------
class ContactDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    PhoneNO=models.IntegerField(null=True,blank=True)
    # ------------------------------------------------------------------------------------------------------
class RegisterDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)
    # ------------------------------------------------------------------------------------------------------
class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField( null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField( null=True, blank=True)
    Prod_Image = models.ImageField(upload_to="Cart Image", null=True, blank=True)

# ------------------------------------------------------------------------------------------------------
class OrderDB(models.Model):
    First_Name= models.CharField(max_length=100, null=True, blank=True)
    Last_Name= models.CharField(max_length=100, null=True, blank=True)
    Email= models.EmailField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Address= models.CharField(max_length=100, null=True, blank=True)
    Mobile= models.CharField(max_length=100, null=True, blank=True)
    State= models.CharField(max_length=100, null=True, blank=True)
    pin=models.IntegerField( null=True, blank=True)
    Total_price=models.IntegerField( null=True, blank=True)
    # ------------------------------------------------------------------------------------------------------

class ClientDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    Client_Image =  models.ImageField(upload_to="client profiles", null=True, blank=True)