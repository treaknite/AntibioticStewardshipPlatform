# Generated by Django 2.2.7 on 2020-01-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200128_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='ag_3',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]