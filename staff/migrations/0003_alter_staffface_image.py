# Generated by Django 5.1.1 on 2024-10-02 01:06

import staff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staff_address_alter_staff_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffface',
            name='image',
            field=models.ImageField(upload_to=staff.models.staff_directory_path),
        ),
    ]