# Generated by Django 5.1.1 on 2024-10-01 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StaffFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
    ]