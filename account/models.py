from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    ADMIN = 'admin'
    MANAGER = 'manager'
    CLIENT = 'client'

    CHOICES_STATUS = (
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
        (CLIENT, "Client"),
    )
    username = models.CharField(max_length=255,unique=True)
    user_role= models.CharField(max_length=10,choices=CHOICES_STATUS, default=CLIENT )
    email = models.EmailField()
    phone = models.CharField(max_length=32)
