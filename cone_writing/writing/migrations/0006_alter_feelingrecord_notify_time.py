# Generated by Django 4.2.5 on 2024-05-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0005_alter_feelingrecord_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feelingrecord',
            name='notify_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='通知时间'),
        ),
    ]