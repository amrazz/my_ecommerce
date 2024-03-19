from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    discription = models.TextField(blank = True)
    cat_image = models.ImageField(upload_to= 'static/images/categories', blank = True)
    is_listed = models.BooleanField(default = True)
    is_deleted = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        

    def __str__(self) :
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    discription = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to= 'static/images/prooduct')
    stock_quantity = models.IntegerField(default = 0)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)
    is_listed = models.BooleanField(default = True)
    is_deleted = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    

    