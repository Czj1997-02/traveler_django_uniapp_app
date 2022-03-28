# Generated by Django 3.0 on 2021-10-01 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20210923_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='path',
            field=models.FileField(blank=True, help_text='文件路径（FileField）', null=True, upload_to='files/2021_10', verbose_name='文件路径'),
        ),
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(blank=True, help_text='图片（ImageField）', null=True, upload_to='imgs/2021_10', verbose_name='图片'),
        ),
    ]
