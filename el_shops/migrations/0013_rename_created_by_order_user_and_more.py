# Generated by Django 4.1.1 on 2022-12-15 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('el_shops', '0012_orderproduct_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='created_by',
            new_name='user',
        ),
    ]
