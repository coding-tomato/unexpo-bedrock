# Generated by Django 3.0.4 on 2020-03-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
