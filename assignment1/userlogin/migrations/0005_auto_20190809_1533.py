# Generated by Django 2.2.4 on 2019-08-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_auto_20190809_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='phonenumber',
            field=models.BigIntegerField(null=True),
        ),
    ]
