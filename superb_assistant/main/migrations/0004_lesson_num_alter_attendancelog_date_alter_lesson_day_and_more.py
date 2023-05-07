# Generated by Django 4.2 on 2023-05-06 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_lesson_room_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendancelog',
            name='date',
            field=models.DateField(default=datetime.date(2023, 5, 6)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='day',
            field=models.SmallIntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')]),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='room_num',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]