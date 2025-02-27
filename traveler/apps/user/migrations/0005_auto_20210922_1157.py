# Generated by Django 3.0 on 2021-09-22 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210922_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='city',
            name='province',
        ),
        migrations.AddField(
            model_name='city',
            name='level',
            field=models.PositiveIntegerField(blank=True, help_text='层级（PositiveIntegerField）', null=True, verbose_name='层级'),
        ),
        migrations.AddField(
            model_name='city',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='child', to='user.City', verbose_name='父级'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(help_text='名称（CharField）', max_length=225, verbose_name='名称'),
        ),
    ]
