# Generated by Django 5.0.4 on 2024-04-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_post_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
