# Generated by Django 5.0 on 2024-09-21 06:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_compositeitem_associatedservice_associateditem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemgroup',
            name='attributes',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
