from django.db import models
from django.contrib.auth.models import AbstractUser
from ..core.models import TimestampMixin


# Create your models here.
class User(AbstractUser, TimestampMixin):
    pass
