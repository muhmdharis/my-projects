# Generated by Django 5.0.6 on 2024-05-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_cart_discription_remove_cart_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discription',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]