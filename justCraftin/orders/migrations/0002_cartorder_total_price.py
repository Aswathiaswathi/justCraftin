# Generated by Django 5.1 on 2024-08-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='total_price',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]