# Generated by Django 4.2.3 on 2023-07-16 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_payments_payment_upi_id_alter_wallet_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'get_latest_by': 'created_at'},
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_status',
            field=models.CharField(choices=[('pending', 'pending'), ('success', 'rejected'), ('rejected', 'rejected')], default='pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_channel',
            field=models.CharField(choices=[('upi', 'upi'), ('bank', 'bank')], max_length=10),
        ),
    ]
