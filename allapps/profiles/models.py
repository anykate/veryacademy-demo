from django.db import models
from django.contrib.auth import get_user_model
from ..core.models import TimestampMixin


# Create your models here.
class UserProfile(TimestampMixin):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profiles',
        on_delete=models.CASCADE
    )

    age = models.PositiveIntegerField(blank=True, default=1)

    def __str__(self):
        return self.user.username
