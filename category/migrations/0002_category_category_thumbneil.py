# Generated by Django 3.2 on 2021-08-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_thumbneil',
            field=models.ImageField(default=1, upload_to='category\thumbneil'),
            preserve_default=False,
        ),
    ]