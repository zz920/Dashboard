# Generated by Django 2.2 on 2019-04-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0002_auto_20190413_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='sales',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
