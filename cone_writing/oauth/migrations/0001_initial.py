# Generated by Django 4.2.5 on 2024-05-30 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OauthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.TextField(choices=[('DINGDING', '钉钉')], default='DINGDING', max_length=20, verbose_name='平台')),
                ('oauth_id', models.CharField(max_length=100, verbose_name='Oauth用户ID')),
                ('oauth_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Oauth用户名')),
                ('oauth_detail', models.JSONField(verbose_name='授权信息')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'Oauth用户',
                'verbose_name_plural': 'Oauth用户',
                'db_table': 'oauth_user',
            },
        ),
    ]
