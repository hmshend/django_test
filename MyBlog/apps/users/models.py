from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as _UserManager
# Create your models here.

class UserManager(_UserManager):
    """

    """
    def create_superuser(self, username, password, email=None, **extra_fields):
        super(UserManager, self).create_superuser(username=username,
                                                  password=password,
                                                  email=email,
                                                  **extra_fields)


class User(AbstractUser):
    """
    add mobile、email_active fields to Django users modules.
    """
    REQUIRED_FIELDS = ['mobile']
    object = UserManager()
    mobile = models.CharField(max_length=11, unique=True, help_text="手机号", verbose_name="手机号",
                              error_messages={
                                  'unique': "此手机号已经注册"
                              })
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')
    class Meta:
        db_table = 'tb_users'  #表名字
        verbose_name = '用户'  #admin站点显示中文信息
        verbose_name_plural = verbose_name  #复数形式

    def __str__(self):
        return self.username

