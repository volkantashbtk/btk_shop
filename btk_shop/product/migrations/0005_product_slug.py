# Generated by Django 4.2.6 on 2023-11-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
