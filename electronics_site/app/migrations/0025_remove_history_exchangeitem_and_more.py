# Generated by Django 5.0.6 on 2024-05-28 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_historyexchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='Exchangeitem',
        ),
        migrations.RemoveField(
            model_name='history',
            name='exchangeDate',
        ),
        migrations.RemoveField(
            model_name='history',
            name='exchangeRate',
        ),
        migrations.RemoveField(
            model_name='history',
            name='withdrawAmount',
        ),
        migrations.RemoveField(
            model_name='historyexchange',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='historyexchange',
            name='premiumState',
        ),
        migrations.RemoveField(
            model_name='historyexchange',
            name='startDate',
        ),
        migrations.RemoveField(
            model_name='historyexchange',
            name='withdrawAmount',
        ),
    ]
