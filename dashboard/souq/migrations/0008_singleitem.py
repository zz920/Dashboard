# Generated by Django 2.1 on 2019-04-24 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0007_merge_20190420_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleItem',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('souq.item',),
        ),
    ]
