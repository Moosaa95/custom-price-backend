# from django.db import models

# # Create your models here.

# class Product(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    
# class Option(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     values = models.CharField(max_length=255)

#     def __str__(self):
#         return self.product

# class Price(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     options = models.JSONField(default=dict)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)


#     def __str__(self):
#         return f'{self.product} {self.price}'
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    @classmethod
    def get_option_price(cls, product_id, option_name):
        try:
            product = cls.objects.get(id=product_id)
            option = product.options.get(name=option_name)
            return option.price
        except (cls.DoesNotExist, Option.DoesNotExist):
            return None
    
    @classmethod
    def get_products(cls):
        fields = [
            "id",
            "name",
            "price"
        ]
        products = cls.objects.all().values(*fields)
        return products

class Option(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')


    def __str__(self):
        return f"{self.name}"