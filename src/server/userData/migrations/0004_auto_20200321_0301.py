# Generated by Django 3.0.4 on 2020-03-21 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userHome', '0004_remove_userhome_userdata'),
        ('userData', '0003_userdata_home'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
        migrations.AddField(
            model_name='userdata',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersdata', to='userHome.UserHome'),
        ),
    ]
