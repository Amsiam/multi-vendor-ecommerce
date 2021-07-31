from django.db import models

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    category_thumbneil = models.ImageField(upload_to="category\thumbneil" , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class ProductCategoryModel(models.Manager):
    def get_queryset(self):
        return super(ProductCategoryModel,self).get_queryset().filter(parent__isnull=True)


class ProductCategory(Category):
    objects = ProductCategoryModel()
    class Meta:
        proxy = True

        verbose_name_plural = "Product Categories"






class ProductSubCategoryModel(models.Manager):
    def get_queryset(self):
        return super(ProductSubCategoryModel,self).get_queryset().filter(parent__isnull=False)


class ProductSubCategory(Category):
    objects = ProductSubCategoryModel()
    class Meta:
        proxy = True
        verbose_name_plural = "Product Sub Categories"