# Generated by Django 3.2.5 on 2021-07-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
