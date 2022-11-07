from django.db import models

# Create your models here.


class CategoryProd(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "categoryProd"
        verbose_name_plural = "categoriesProd"


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryProd, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="StoreApp")
    description = models.CharField(max_length=300)
    platform = models.CharField(max_length=50)
    classification = models.CharField(max_length=20)
    price = models.FloatField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"