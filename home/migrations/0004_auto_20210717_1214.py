# Generated by Django 3.2.4 on 2021-07-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='binding',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_range',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
