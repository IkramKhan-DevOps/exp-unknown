from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
# Create your models here.
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(max_length=20, unique=True)
    is_customer = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'


class Profile(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Custom', 'Custom'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=20)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
