from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registed_dttm = models.DateTimeField(auto_now_add=True,
                                        verbose_name='등록시간')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '테스트 페이지 태그'
        verbose_name_plural ='테스트 페이지 태그'
        