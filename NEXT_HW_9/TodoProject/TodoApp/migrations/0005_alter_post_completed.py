# Generated by Django 5.0.4 on 2024-04-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0004_alter_post_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]