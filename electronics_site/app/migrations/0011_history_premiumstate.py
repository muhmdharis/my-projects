# Generated by Django 5.0.6 on 2024-05-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_history_withdrawamount_alter_history_enddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='premiumState',
            field=models.CharField(default='False', max_length=1000, null=True),
        ),
    ]
