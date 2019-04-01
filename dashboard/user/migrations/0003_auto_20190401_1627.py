# Generated by Django 2.1.7 on 2019-04-01 16:27

import common.enum.role
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190401_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.CharField(choices=[(common.enum.role.SystemValidRole('ADMIN'), 'ADMIN'), (common.enum.role.SystemValidRole('MANAGER'), 'MANAGER'), (common.enum.role.SystemValidRole('CUSTOMER_SERVICE_STUFF'), 'CUSTOMER_SERVICE_STUFF'), (common.enum.role.SystemValidRole('CUSTOMER_LEVLE_1'), 'CUSTOMER_LEVLE_1'), (common.enum.role.SystemValidRole('CUSTOMER_LEVLE_2'), 'CUSTOMER_LEVLE_2'), (common.enum.role.SystemValidRole('CUSTOMER_LEVLE_3'), 'CUSTOMER_LEVLE_3'), (common.enum.role.SystemValidRole('CUSTOMER_LEVLE_4'), 'CUSTOMER_LEVLE_4'), (common.enum.role.SystemValidRole('VISITOR'), 'VISITOR')], default=common.enum.role.SystemValidRole('VISITOR'), max_length=50),
        ),
    ]
