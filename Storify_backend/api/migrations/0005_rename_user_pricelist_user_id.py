# Generated by Django 5.0 on 2024-09-21 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pricelist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricelist',
            old_name='user',
            new_name='user_id',
        ),
    ]
