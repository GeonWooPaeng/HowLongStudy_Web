from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32,
                                    verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                    verbose_name='비밀번호')

    
    def __str__(self):
        return self.username 

    class Meta:
        db_table = 'MLS_user'
        verbose_name = 'MLS_user'
        verbose_name_plural = 'MLS_user'

        