from django.db import models
from django.contrib.auth.models import User
# Create   your models here.

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1'
    )
    prod_code=models.IntegerField(default=100)
    for_user=models.CharField(max_length=100,default="xyz")    
    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(
        max_length=500,
        default='''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Facilis quae nemo ducimus, aperiam reprehenderit sit provident quam, enim tempore ea eligendi vel facere? In numquam deleniti, debitis quod odit tenetur.'''
        )
    item_price=models.IntegerField()
    item_image=models.CharField(
        max_length=500,
        default="https://assets.materialup.com/uploads/b03b23aa-aa69-4657-aa5e-fa5fef2c76e8/preview.png"
    )
    def __str__(self):
        return self.item_name
       