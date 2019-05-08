# Generated by Django 2.1.7 on 2019-05-05 19:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_eventcard_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
