# Generated by Django 3.0.4 on 2020-03-21 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nums', '0002_auto_20200310_2049'),
        ('logs', '0004_auto_20200309_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='nums.Number'),
        ),
    ]
