# Generated by Django 5.0.6 on 2024-05-13 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_image_url_post_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 16, 11, 26, 103031)),
        ),
    ]
