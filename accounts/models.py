import os
from datetime import datetime
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def profile_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(
        'profiles','images',filename
    )

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey(to='City',related_name='user_city',on_delete=models.CASCADE ,blank=True,null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to=profile_image_upload_to, default='default.png')

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name