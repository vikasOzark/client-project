# Generated by Django 4.2.3 on 2023-07-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_payments_payment_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_type',
            field=models.CharField(choices=[('DEPOSIT', 'DEPOSIT'), ('WITHDRAWAL', 'WITHDRAWAL')], max_length=25),
        ),
    ]
