# Generated by Django 4.1 on 2022-09-18 16:42

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('is_ordered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('catogary', models.CharField(choices=[('Phones', 'Phones'), ('Laptops', 'Laptops'), ('Tablets', 'Tablets'), ('Desktop pc', 'Desktop pc')], max_length=255)),
                ('brand', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Sony', 'Sony'), ('Lenovo', 'Lenovo'), ('Moto', 'Moto')], max_length=255)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cpu', models.CharField(max_length=255)),
                ('system', models.CharField(choices=[('Android', 'Android'), ('iOS', 'iOS'), ('Windows', 'Windows'), ('Linux', 'Linux'), ('MacOS', 'MacOS'), ('iPadOS', 'iPadOS'), ('Chrome OS', 'Chrome OS')], max_length=255)),
                ('is_best_selling', models.BooleanField(default=False)),
                ('is_trending_now', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(choices=[('Al Anbar', 'Al Anbar'), ('Al Muthanna', 'Al Muthanna'), ('Al-Qadisiyyah', 'Al-Qadisiyyah'), ('Babylon', 'Babylon'), ('Baghdad', 'Baghdad'), ('Basra', 'Basra'), ('Dhi Qar', 'Dhi Qar'), ('Dihok', 'Dihok'), ('Diyala', 'Diyala'), ('Erbil', 'Erbil'), ('Karbala', 'Karbala'), ('Kirkuk', 'Kirkuk'), ('Maysan', 'Maysan'), ('Najaf', 'Najaf'), ('Nineveh', 'Nineveh'), ('Saladin', 'Saladin'), ('Sulaymaniyah', 'Sulaymaniyah'), ('Wasit', 'Wasit')], default='Baghdad', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductRamAndStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rams_and_storage', to='eCommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='eCommerce.product')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='eCommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Order Taken', 'Order Taken'), ('Order is Being Prepared', 'Order is Being Prepared'), ('Order Is Being Delivered', 'Order Is Being Delivered'), ('Order Received', 'S4')], max_length=255)),
                ('is_ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(related_name='order', to='eCommerce.item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='eCommerce.product'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='eCommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
