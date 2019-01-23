from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

class User(AbstractUser):
    email = models.EmailField('電子郵件', unique=True)
    is_public = models.BooleanField('公開帳號', default=True)
    introduction = models.TextField('自我介紹', blank=True)


class Relationship(models.Model):
                      #ForeignKey -- 從USER這張表獲取他的PK
    from_user = models.ForeignKey(User,  models.CASCADE, verbose_name='從', related_name='following')
    to_user = models.ForeignKey(User, models.CASCADE, verbose_name='到', related_name='follower')
    is_agree = models.BooleanField('同意', default=False)
    is_delete = models.BooleanField('刪除', default=False)
    start_at = models.DateField('開始時間', auto_now=True)

    class Meta:
        unique_together=[
            ['from_user', 'to_user']
        ]

    def __str__(self):
        return 'From {} to {}'.format(self.from_user.username, self.to_user.username)

    def clean(self):
        if self.from_user_id == self.to_user_id:
            raise ValidationError('不可追蹤自己')
