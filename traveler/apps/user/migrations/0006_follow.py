# Generated by Django 3.0 on 2021-10-01 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210922_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='创建时间（DateTimeField）', null=True, verbose_name='创建时间')),
                ('last_edited_date', models.DateTimeField(auto_now=True, help_text='最后编辑时间（DateTimeField）', null=True, verbose_name='最后编辑时间')),
                ('deleted', models.CharField(choices=[('0', '未删除'), ('1', '已删除')], default='0', help_text='是否删除（CharField，可选值：0，1）', max_length=1, verbose_name='是否删除')),
                ('created_by', models.ForeignKey(blank=True, help_text='创建人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow_cb', to='user.UserExtension', verbose_name='创建人ID')),
                ('follow', models.ForeignKey(blank=True, help_text='关注（ForeignKey）', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow', to='user.UserExtension', verbose_name='关注')),
                ('last_edited_by', models.ForeignKey(blank=True, help_text='最后编辑人ID（ForeignKey）', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow_eb', to='user.UserExtension', verbose_name='最后编辑人ID')),
            ],
            options={
                'verbose_name': '用户关注',
                'verbose_name_plural': '用户关注',
                'unique_together': {('follow', 'created_by')},
            },
        ),
    ]
