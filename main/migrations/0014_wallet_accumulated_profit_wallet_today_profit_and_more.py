# Generated by Django 4.2.3 on 2023-07-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_bankdetail_user_alter_payments_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='accumulated_profit',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='wallet',
            name='today_profit',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='wallet',
            name='yesterday_profit',
            field=models.CharField(default=0, max_length=10),
        ),
    ]