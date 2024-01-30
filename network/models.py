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
    # 'related_name' defines the reverse relationship.
    # e.g if x is following y, y's follower will be x
    # 'symmetrical=False' is saying that a following b
    # doesn't automatically mean b is following a
    followers = models.ManyToManyField('self', symmetrical=False, related_name="following") 
    following = models.ManyToManyField('self', symmetrical=False, related_name="followers")

    def natural_key(self):
        return (self.username)

class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,