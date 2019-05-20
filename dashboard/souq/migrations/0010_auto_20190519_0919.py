# Generated by Django 2.1 on 2019-05-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0009_singlecategory_singleseller'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='hotitem',
            options={'verbose_name': 'Hot Item', 'verbose_name_plural': 'Hot Item'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'seller', 'verbose_name_plural': 'sellers'},
        ),
        migrations.AlterModelOptions(
            name='singlecategory',
            options={'verbose_name': 'single category', 'verbose_name_plural': 'single category'},
        ),
        migrations.AlterModelOptions(
            name='singleitem',
            options={'verbose_name': 'single item', 'verbose_name_plural': 'single item'},
        ),
        migrations.AlterModelOptions(
            name='singleseller',
            options={'verbose_name': 'single seller', 'verbose_name_plural': 'single seller'},
        ),
        migrations.AlterField(
            model_name='category',
            name='classification',
            field=models.CharField(max_length=50, verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='category',
            name='link',
            field=models.CharField(max_length=250, unique=True, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ean_code',
            field=models.CharField(max_length=50, verbose_name='EAN'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img_link',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='image link'),
        ),
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.CharField(max_length=1000, verbose_name='item link'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='item name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='plantform',
            field=models.CharField(max_length=20, verbose_name='plantform'),
        ),
        migrations.AlterField(
            model_name='item',
            name='trace_id',
            field=models.CharField(max_length=30, verbose_name='item id'),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_id',
            field=models.CharField(max_length=30, unique=True, verbose_name='unit id'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='link',
            field=models.CharField(max_length=250, unique=True, verbose_name='seller link'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=50, verbose_name='seller name'),
        ),
        migrations.AddIndex(
            model_name='detail',
            index=models.Index(fields=['sales'], name='souq_detail_sales_1cde3a_idx'),
        ),
        migrations.AddIndex(
            model_name='detail',
            index=models.Index(fields=['created'], name='souq_detail_created_0b851c_idx'),
        ),
        migrations.AddIndex(
            model_name='detail',
            index=models.Index(fields=['price'], name='souq_detail_price_21ea63_idx'),
        ),
    ]