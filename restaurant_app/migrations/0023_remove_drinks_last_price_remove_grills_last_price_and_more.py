# Generated by Django 5.1.5 on 2025-02-20 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0022_alter_cartitem_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinks',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='grills',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='grills',
            name='size',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='meals',
            name='size',
        ),
        migrations.RemoveField(
            model_name='salads',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='sandwiches',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='sandwiches',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sweets',
            name='last_price',
        ),
        migrations.RemoveField(
            model_name='sweets',
            name='size',
        ),
    ]
