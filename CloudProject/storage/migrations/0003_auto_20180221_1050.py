# Generated by Django 2.0.2 on 2018-02-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20180217_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
