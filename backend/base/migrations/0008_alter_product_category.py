# Generated by Django 4.1.3 on 2023-02-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_orderitem_order_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('CLOTHS', 'CLOTHS'), ('SHOES', 'SHOES'), ('BAGS', 'BAGS'), ('WATCHES', 'WATCHES'), ('ELECTRONICS', 'ELECTRONICS')], max_length=200),
        ),
    ]