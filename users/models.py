from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AppUserManager
import uuid
from django.core.validators import MinLengthValidator
from django.contrib.sessions.models import Session

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = AppUserManager()

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(AppUser, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=50, validators=[MinLengthValidator(5)])
    credits = models.IntegerField(default=0)
    last_wheel_spin = models.DateTimeField(null=True, blank=True)
    is_wheel_available = models.BooleanField(default=True)


    @property
    def customer_credits(self):
        print(self.credits)
        return "{:,}".format(self.credits)

    def __str__(self) -> str:
        return self.name

class UserSession(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
