# Generated by Django 3.0.4 on 2020-03-22 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userData', '0005_auto_20200322_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='home',
        ),
    ]
