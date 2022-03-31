from django.db import models

# this database will be used to store data of users
# i will change chis database in future
class userData(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30, default='abc')
    email = models.CharField(max_length=50, default='abc@gmail.com')
    password = models.CharField(max_length=20, default='123abc')
    def __str__(self):
        return self.username

# database for storing products details
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='kite/photos', default='')
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name