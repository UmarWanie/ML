# Generated by Django 2.2.5 on 2021-02-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210220_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')], default=2, max_length=2),
        ),
    ]