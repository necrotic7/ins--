from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('電子郵件')
    is_public = models.BooleanField('公開帳號', default=True)
