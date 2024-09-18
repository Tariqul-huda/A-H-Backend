from django.db import models
class Category(models.Model):

    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Product(models.Model):

    product_name = models.CharField(help_text="Set the product name", max_length=50,null = False)
    product_description = models.CharField(help_text="Give the description of the product", max_length=1000,null=False)
    product_price = models.FloatField(help_text="Set the price for the product", null=False)
    product_image_url = models.CharField(help_text="Image URL of a product",null = False,max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

