from django.contrib.auth.models import AbstractUser
from django.db import models

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value) cannot be negative'),
            params={'value': value},
        )

# Define this to help retrieve User's username in serialization
class UserManager(models.Manager):
    def get_by_natural_key(self, username):
     