from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        blank=True
    )
    gender = models.CharField(
        max_length=10,
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ),
        blank=True
    )
    languages = models.CharField(
        max_length=100,
        blank=True
    )
    online_status = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.user.username
