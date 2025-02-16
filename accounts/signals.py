from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account

# Create or Update Account when User is saved
@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    if created:
        # Create a new account if user is newly created
        Account.objects.create(user=instance)
    else:
        # Update the account when user changes
        instance.account.save()

# Delete Account when User is deleted
@receiver(post_delete, sender=User)
def delete_user_account(sender, instance, **kwargs):
    try:
        instance.account.delete()  # Delete the linked account
    except Account.DoesNotExist:
        pass  # Ignore if account doesn't exist

