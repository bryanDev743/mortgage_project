# Generated by Django 4.0.3 on 2022-05-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]