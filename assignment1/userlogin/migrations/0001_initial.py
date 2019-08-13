# Generated by Django 2.2.4 on 2019-08-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('phonenumber', models.IntegerField()),
                ('address', models.TextField(max_length=80)),
            ],
            options={
                'db_table': 'userlogin',
            },
        ),
    ]