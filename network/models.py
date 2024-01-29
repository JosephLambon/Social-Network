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
        return self.get(username=username)

class User(AbstractUser):
    def natural_key(self):
        return (self.username)
    pass

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    likes = models.IntegerField(default=0, validators=[validate_positive])

    # Format DateTime object as desired
    def timestamp(self):
        return self.created.strftime('%d/%m/%y %I:%M %p')
        