# Generated by Django 2.1.7 on 2019-04-03 18:56

from django.db import migrations
import user.models_content.user


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models_content.user.UserAuthManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
