# Generated by Django 2.1.5 on 2019-07-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20190719_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
