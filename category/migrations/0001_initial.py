# Generated by Django 3.2.5 on 2021-07-31 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Product Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('category.category',),
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Product Sub Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('category.category',),
        ),
    ]
