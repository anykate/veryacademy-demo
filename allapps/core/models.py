from django.db import models
from django.db.models import Prefetch


# Create your models here.
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Language(TimestampMixin):
    lname = models.CharField(max_length=10)

    def __str__(self):
        return self.lname


class Framework(TimestampMixin):
    fname = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname
