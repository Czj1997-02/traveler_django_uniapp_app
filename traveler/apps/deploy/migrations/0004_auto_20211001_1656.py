# Generated by Django 3.0 on 2021-10-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20210926_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swiper',
            name='img',
            field=models.ImageField(blank=True, help_text='图片（ImageField）', null=True, upload_to='imgs/2021_10', verbose_name='图片'),
        ),
    ]
