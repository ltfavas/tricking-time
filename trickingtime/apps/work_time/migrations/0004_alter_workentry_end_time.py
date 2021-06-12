# Generated by Django 3.2.4 on 2021-06-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_time', '0003_auto_20210610_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workentry',
            name='end_time',
            field=models.TimeField(blank=True, help_text='The hour and minutes in which the activity was ended', null=True, verbose_name='End'),
        ),
    ]