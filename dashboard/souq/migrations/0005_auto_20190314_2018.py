# Generated by Django 2.1.7 on 2019-03-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0004_auto_20190314_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souqitem',
            name='link',
            field=models.CharField(db_index=True, max_length=1000),
        ),
    ]
