# Generated by Django 3.1.4 on 2022-02-16 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0006_auto_20220215_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymembers',
            name='date_of_init',
        ),
        migrations.AlterField(
            model_name='familyhead',
            name='date_of_init',
            field=models.DateField(default=datetime.date(2022, 2, 16)),
        ),
    ]
