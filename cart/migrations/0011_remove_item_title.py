# Generated by Django 3.1.7 on 2021-08-13 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_item_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
    ]