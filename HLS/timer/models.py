from django.db import models

# Create your models here.

class Timer(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    study_time = models.TimeField(verbose_name='공부시간')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'timer'
        verbose_name = '공부시간'
        verbose_name_plural = '공부시간'