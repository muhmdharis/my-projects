# Generated by Django 5.0.6 on 2024-05-28 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_exchange_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='wallet',
        ),
    ]