# Generated by Django 2.2.2 on 2020-05-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200515_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_calculate',
            field=models.IntegerField(default=0),
        ),
    ]
