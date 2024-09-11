from django.db import models

class Category(models.Model):
    category_id = models.IntegerField(help_text="This is category's ID",primary_key=True,null=False)
    category_name = models.CharField(max_length=50)

class Product(models.Model):

    product_id = models.IntegerField(help_text="This is product's ID",primary_key=True)
    product_price = models.FloatField(help_text="Set the price for the product", null=False)
    product_description = models.CharField(help_text="Give the description of the product", max_length=1000,null=False)
    product_name = models.CharField(help_text="Set the product name", max_length=50,null = False)
    product_image_url = models.CharField(help_text="Image URL of a product",null = False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

