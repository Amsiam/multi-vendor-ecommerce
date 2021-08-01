# Generated by Django 3.2.5 on 2021-08-01 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0003_alter_category_category_thumbneil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('in_stock', models.IntegerField()),
                ('thumbnail', models.ImageField(upload_to='product/thumbnail')),
                ('slug', models.SlugField()),
                ('discount_type', models.CharField(choices=[('M', 'Money'), ('P', 'Percent'), ('N', 'None')], default='N', max_length=1)),
                ('discount', models.FloatField(blank=True)),
                ('discount_start', models.DateTimeField(blank=True)),
                ('discount_end', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product/thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
