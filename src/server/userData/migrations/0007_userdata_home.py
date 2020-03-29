# Generated by Django 3.0.4 on 2020-03-23 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userHome', '0006_remove_userhome_user'),
        ('userData', '0006_remove_userdata_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersdata', to='userHome.UserHome'),
        ),
    ]
