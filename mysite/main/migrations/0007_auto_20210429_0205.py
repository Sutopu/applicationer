# Generated by Django 3.1.1 on 2021-04-29 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210429_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_applied',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Applied'),
        ),
    ]
