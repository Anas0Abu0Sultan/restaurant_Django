# Generated by Django 5.1.5 on 2025-03-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0030_contact_general_whatsapp_contact_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='telegram',
        ),
        migrations.AddField(
            model_name='contact',
            name='telegram_username',
            field=models.CharField(default='Eng_Anas_Sultan', max_length=50),
        ),
    ]
