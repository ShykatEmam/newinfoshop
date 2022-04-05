import uuid
from django.db import models
from django.db.models import Model

# Create your models here.

class Feature(models.Model):
    name: models.CharField(max_length=100)
    details: models.CharField(max_length=500)
    def __str__(self):
        return self.name
class ShoppingMalls(models.Model):
   #owner
    shopping_mall_name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    address = models.TextField(null=False)
    
    category_1 = models.CharField(max_length=200,null=True,blank=True)
    category_2 = models.CharField(max_length=200,null=True,blank=True)
    category_3 = models.CharField(max_length=200,null=True,blank=True)
    category_4 = models.CharField(max_length=200,null=True,blank=True)
    category_5 = models.CharField(max_length=200,null=True,blank=True)
    category_6 = models.CharField(max_length=200,null=True,blank=True)
    category_7 = models.CharField(max_length=200,null=True,blank=True)
    # featured_image
    
    gmail_link = models.CharField(max_length=1000,null=True,blank=True)
    website_link = models.CharField(max_length=1000,null=True,blank=True)
    facebook_link = models.CharField(max_length=1000,null=True,blank=True)
    other_link = models.CharField(max_length=1000,null=True,blank=True)
    
    phone_1 = models.CharField(max_length=50,null=True,blank=True)
    phone_2 = models.CharField(max_length=50,null=True,blank=True)
    phone_3 = models.CharField(max_length=50,null=True,blank=True)
    phone_4 = models.CharField(max_length=50,null=True,blank=True)
    
    facilities_1 = models.CharField(max_length=200,null=True,blank=True)
    facilities_2 = models.CharField(max_length=200,null=True,blank=True)
    facilities_3 = models.CharField(max_length=200,null=True,blank=True)
    facilities_4 = models.CharField(max_length=200,null=True,blank=True)
    facilities_5 = models.CharField(max_length=200,null=True,blank=True)
    facilities_6 = models.CharField(max_length=200,null=True,blank=True)
    facilities_7 = models.CharField(max_length=200,null=True,blank=True)
    facilities_8 = models.CharField(max_length=200,null=True,blank=True)
    facilities_9 = models.CharField(max_length=200,null=True,blank=True)
    facilities_10 = models.CharField(max_length=200,null=True,blank=True)
    facilities_11 = models.CharField(max_length=200,null=True,blank=True)
    facilities_12 = models.CharField(max_length=200,null=True,blank=True)
    facilities_13 = models.CharField(max_length=200,null=True,blank=True)
    facilities_14 = models.CharField(max_length=200,null=True,blank=True)
    facilities_15 = models.CharField(max_length=200,null=True,blank=True)

    floors_1 = models.CharField(max_length=200,null=True,blank=True)
    floors_2 = models.CharField(max_length=200,null=True,blank=True)
    floors_3 = models.CharField(max_length=200,null=True,blank=True)
    floors_4 = models.CharField(max_length=200,null=True,blank=True)
    floors_5 = models.CharField(max_length=200,null=True,blank=True)
    floors_6 = models.CharField(max_length=200,null=True,blank=True)
    floors_7 = models.CharField(max_length=200,null=True,blank=True)
    floors_8 = models.CharField(max_length=200,null=True,blank=True)
    floors_9 = models.CharField(max_length=200,null=True,blank=True)
    floors_10 = models.CharField(max_length=200,null=True,blank=True)
    floors_11 = models.CharField(max_length=200,null=True,blank=True)
    floors_12 = models.CharField(max_length=200,null=True,blank=True)

    division = models.CharField(max_length=200)
    image_0 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_1 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_2 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_3 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_4 = models.ImageField(upload_to='uploads/',null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.shopping_mall_name

class Brands(models.Model):
       #owner
    brand_name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    
    category_1 = models.CharField(max_length=200,null=True,blank=True)
    category_2 = models.CharField(max_length=200,null=True,blank=True)
    category_3 = models.CharField(max_length=200,null=True,blank=True)
    category_4 = models.CharField(max_length=200,null=True,blank=True)
    category_5 = models.CharField(max_length=200,null=True,blank=True)
    category_6 = models.CharField(max_length=200,null=True,blank=True)
    category_7 = models.CharField(max_length=200,null=True,blank=True)
    # featured_image
    
    gmail_link = models.CharField(max_length=1000,null=True,blank=True)
    website_link = models.CharField(max_length=1000,null=True,blank=True)
    facebook_link = models.CharField(max_length=1000,null=True,blank=True)
    other_link = models.CharField(max_length=1000,null=True,blank=True)
    

    showrooms_1 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_1 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_2 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_2 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_3 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_3 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_4 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_4 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_5 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_5 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_6 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_6 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_7 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_7 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_8 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_8 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_9 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_9 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_10 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_10 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_11 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_11 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_12 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_12 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_13 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_13 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_14 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_14 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_15 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_15 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_16 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_16 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_17 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_17 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_18 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_18 = models.CharField(max_length=50,null=True,blank=True)
    showrooms_19 = models.CharField(max_length=200,null=True,blank=True)
    showrooms_phone_19 = models.CharField(max_length=50,null=True,blank=True)

    image_0 = models.ImageField(upload_to='uploads/',null=True)
    image_1 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_2 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_3 = models.ImageField(upload_to='uploads/',null=True,blank=True)
    image_4 = models.ImageField(upload_to='uploads/',null=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.brand_name