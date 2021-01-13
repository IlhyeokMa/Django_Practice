from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=32,
                                verbose_name='비밀번호')
    registed_dttm = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록시간')

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '테스트 페이지 사용자'
        verbose_name_plural ='테스트 페이지 이용자'
        