# Generated by Django 4.2.6 on 2023-11-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, upload_to='products_images')),
                ('product_discount_price', models.FloatField()),
                ('product_original_price', models.FloatField()),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]