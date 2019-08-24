# Generated by Django 2.2.4 on 2019-08-24 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neptourapp', '0005_post_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourist',
            name='dob',
        ),
        migrations.AddField(
            model_name='photographer',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourist',
            name='username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
