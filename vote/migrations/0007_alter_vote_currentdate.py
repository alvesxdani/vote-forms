# Generated by Django 4.1 on 2022-09-14 01:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_alter_vote_currentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='currentDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 22, 21, 19, 178011)),
        ),
    ]
