from django.db import models

# Create your models here.

class Timer(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    study_day = models.IntegerField(verbose_name='공부한 날')
    study_hour = models.IntegerField(verbose_name='시간')
    study_min = models.IntegerField(verbose_name='분')
    study_sec = models.IntegerField(verbose_name='초')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.user) + str(self.study_day) + str(self.study_hour) + str(self.study_min) + str(self.study_sec)

    class Meta:
        db_table = 'timer'
        verbose_name = '공부시간'
        verbose_name_plural = '공부시간'
