# Generated by Django 5.0.6 on 2024-05-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='withdrawAmount',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='endDate',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='startDate',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]