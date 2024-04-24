# Generated by Django 5.0.4 on 2024-04-23 08:57

import clothes.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='colors/')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image1', models.ImageField(null=True, upload_to='colors/')),
                ('image2', models.ImageField(null=True, upload_to='colors/')),
                ('image3', models.ImageField(null=True, upload_to='colors/')),
                ('image4', models.ImageField(null=True, upload_to='colors/')),
                ('material', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('design', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('مردانه', 'مردانه'), ('زنانه', 'زنانه')], max_length=10)),
                ('color', models.ManyToManyField(to='clothes.color')),
                ('sizes', models.ManyToManyField(to='clothes.size')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to=clothes.models.get_image_path)),
                ('name', models.OneToOneField(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.clothing')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('delivery_address', models.TextField(default='خراسان رضوی-مشهد', max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.color')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.clothing')),
                ('user', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.size')),
            ],
        ),
    ]
