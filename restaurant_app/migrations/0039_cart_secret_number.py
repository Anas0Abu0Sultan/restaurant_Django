# Generated by Django 5.1.5 on 2025-03-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0038_cart_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='secret_number',
            field=models.IntegerField(default=1001),
            preserve_default=False,
        ),
    ]
