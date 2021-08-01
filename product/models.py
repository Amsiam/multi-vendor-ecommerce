from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from category.models import Category

User = get_user_model()


class DiscountType(models.TextChoices):
    money = "M", "Money"
    percent = "P", "Percent"
    none = "N", "None"


class ProductStatus(models.TextChoices):
    PUBLISHED = "PB", "Published"
    DRAFT = "DR", "Draft"


class Product(models.Model):
    # about product
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL, related_name="products")
    status = models.CharField(
        max_length=2, default=ProductStatus.DRAFT, choices=ProductStatus.choices)
    in_stock = models.IntegerField()

    thumbnail = models.ImageField(upload_to="product/thumbnail")
    slug = models.SlugField(unique=True)

    # about seller
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")

    # about discount
    discount_type = models.CharField(
        max_length=1, default=DiscountType.none, choices=DiscountType.choices)
    discount = models.FloatField(blank=True, null=True)
    discount_start = models.DateTimeField(blank=True, null=True)
    discount_end = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if(not self.slug):
            self.slug = slugify(self.title,allow_unicode=True)

            while(Product.objects.filter(slug=self.slug).count()):
                self.slug += "-"+str(len(self.slug))

        return super(Product, self).save(*args, **kwargs)


class ExtraImages(models.Model):

    product = models.ForeignKey(
        "product", on_delete=models.CASCADE, related_name="extraimages")
    images = models.ImageField(upload_to="product/thumbnail")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Extra Image"
        verbose_name_plural = "Extra Images"
