# Generated by Django 5.1.5 on 2025-02-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0009_drinks_category_grills_category_meals_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='text_icon',
            field=models.CharField(default='fa fa-3x fa-cart-plus text-primary mb-4', max_length=2500),
        ),
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.ImageField(default='media/defa/client.png', upload_to='icons/'),
        ),
    ]
