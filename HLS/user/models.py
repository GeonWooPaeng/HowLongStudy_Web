from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    level = models.CharField(max_length=8, verbose_name='등급',
        choices=(
            ('admin', 'admin'),
            ('user', 'user')
        )
    )
    register_data = models.DateField(auto_now_add=True, verbose_name='등록 날짜')

    def __str__(self):
        return self.email 

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'