from django.db import models

class ProductCategory(models.Model):
    brands = models.CharField(max_length=100,null=True,blank=True)
    categories = models.CharField(max_length=100,null=True,blank=True)
    product_type = models.CharField(max_length=100,null=True,blank=True)
    seller = models.CharField(max_length=100,null=True,blank=True)
    warranty = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.brands

    def save(self, *args, **kwargs):
        self.brands = self.brands.lower()
        self.categories = self.categories.lower()
        self.product_type = self.product_type.lower()
        self.seller = self.seller.lower()
        self.warranty = self.warranty.lower()
        return super(ProductCategory, self).save(*args, **kwargs)

class Product(models.Model):
    pd_name = models.CharField(max_length=100)
    price  = models.PositiveIntegerField()
    dis_price = models.PositiveIntegerField()
    product_images = models.ImageField(upload_to="product iamge")
    prodcut_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.pd_name
    
    