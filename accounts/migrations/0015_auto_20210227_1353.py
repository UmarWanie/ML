# Generated by Django 2.2.5 on 2021-02-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210227_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='Gender',
            field=models.IntegerField(default=2),
        ),
    ]
