# Generated by Django 4.2.5 on 2024-05-27 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='事情')),
                ('explain', models.CharField(max_length=500, verbose_name='解释')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('feeling', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='writing.feeling', verbose_name='心情')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='writing.thing')),
            ],
            options={
                'verbose_name': '事情',
                'verbose_name_plural': '事情',
                'db_table': 'user_thing',
                'ordering': ('-id',),
            },
        ),
    ]
