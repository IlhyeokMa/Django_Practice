# Generated by Django 3.1.5 on 2021-01-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20210114_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자 이메일'),
            preserve_default=False,
        ),
    ]
