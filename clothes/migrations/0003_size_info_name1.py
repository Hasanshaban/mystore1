# Generated by Django 5.0.4 on 2024-04-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_size_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='size_info',
            name='name1',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
