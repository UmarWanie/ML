# Generated by Django 2.2.5 on 2021-02-22 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210222_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prediction',
            old_name='patient',
            new_name='user',
        ),
    ]