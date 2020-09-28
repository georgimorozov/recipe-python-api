from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password='none', **extra_fields):
        """
        Creates and saves a new user.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password='none'):
        """
        Create and save a new superuser.
        :param email:
        :param password:
        :return:
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model That Supports Email Instead Of Username
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
