# Generated by Django 4.2.3 on 2023-07-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_payments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_type',
            field=models.CharField(choices=[('DEPOSITE', 'DEPOSITE'), ('WITHDRAWAL', 'WITHDRAWAL')], max_length=25),
        ),
    ]
