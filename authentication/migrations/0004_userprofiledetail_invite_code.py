# Generated by Django 4.2 on 2023-07-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_userprofiledetail_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiledetail',
            name='invite_code',
            field=models.CharField(blank=True, max_length=5, unique=True),
        ),
    ]