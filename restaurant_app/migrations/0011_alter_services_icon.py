# Generated by Django 5.1.5 on 2025-02-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0010_services_text_icon_alter_services_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.ImageField(default='defa/client.png', upload_to='icons/'),
        ),
    ]
