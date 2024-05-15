# Generated by Django 5.0.3 on 2024-04-25 13:52

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 25, 22, 52, 49, 335523)),
        ),
        migrations.AddField(
            model_name='post',
            name='last_viewed_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
