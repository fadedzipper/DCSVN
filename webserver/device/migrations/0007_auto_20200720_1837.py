# Generated by Django 2.2.6 on 2020-07-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0006_auto_20200720_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmdata',
            name='dealwith_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='处理时间'),
        ),
    ]
