# Generated by Django 4.1.1 on 2022-12-15 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('el_shops', '0013_rename_created_by_order_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='created_by',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]
