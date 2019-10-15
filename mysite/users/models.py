from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#########################3
#THIS STUFF will BE USEFUL AFTER i AM ABLE TO BUILD A SIGN UP FORM 

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
##########################3