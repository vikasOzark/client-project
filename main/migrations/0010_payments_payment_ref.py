# Generated by Django 4.2.3 on 2023-07-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_payments_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_ref',
            field=models.CharField(default='', max_length=10),
        ),
    ]