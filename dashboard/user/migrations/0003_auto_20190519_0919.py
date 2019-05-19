# Generated by Django 2.1 on 2019-05-19 09:19

from django.db import migrations
import user.models_content.user


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190403_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSelfInfoProxy',
            fields=[
            ],
            options={
                'verbose_name': 'user detail',
                'verbose_name_plural': 'user detail',
                'proxy': True,
                'indexes': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', user.models_content.user.UserAuthManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
