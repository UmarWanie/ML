# Generated by Django 2.2.5 on 2021-02-22 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20210220_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')], default=2),
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_preg', models.IntegerField(null=True)),
                ('gul', models.IntegerField(null=True)),
                ('bp', models.IntegerField(null=True)),
                ('skt', models.IntegerField(null=True)),
                ('ins', models.IntegerField(null=True)),
                ('BMI', models.IntegerField(null=True)),
                ('ped', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]