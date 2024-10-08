# Generated by Django 5.0 on 2024-09-20 20:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_companyname_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Goods', 'Goods'), ('Service', 'Service')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images/')),
                ('name', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('unit', models.CharField(max_length=50)),
                ('is_returnable', models.BooleanField(default=False)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dimension_unit', models.CharField(choices=[('cm', 'Centimeters'), ('inch', 'Inches')], default='cm', max_length=10)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('weight_unit', models.CharField(choices=[('kg', 'Kilograms'), ('lbs', 'Pounds')], default='kg', max_length=10)),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('upc', models.CharField(blank=True, max_length=100, null=True)),
                ('mpn', models.CharField(blank=True, max_length=100, null=True)),
                ('isbn', models.CharField(blank=True, max_length=100, null=True)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sales_description', models.TextField(blank=True, null=True)),
                ('sales_account', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purchase_description', models.TextField(blank=True, null=True)),
                ('purchase_account', models.CharField(blank=True, max_length=100, null=True)),
                ('inventory_account', models.CharField(blank=True, max_length=100, null=True)),
                ('opening_stock', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('reorder_point', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
