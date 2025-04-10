# Generated by Django 5.1.5 on 2025-02-03 09:00

import restaurant_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0011_alter_services_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefs',
            name='image',
            field=models.ImageField(default='defa/chef.jpg', upload_to='chef/'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='image',
            field=models.ImageField(default='defa/client.png', upload_to='chef/'),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
        migrations.AlterField(
            model_name='grills',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
        migrations.AlterField(
            model_name='rest_detail',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to='restaurant/'),
        ),
        migrations.AlterField(
            model_name='salads',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
        migrations.AlterField(
            model_name='sandwiches',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
        migrations.AlterField(
            model_name='sweets',
            name='image',
            field=models.ImageField(default='defa/defa.png', upload_to=restaurant_app.models.upload_to_dynamic),
        ),
    ]
