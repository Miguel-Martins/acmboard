# Generated by Django 2.1.7 on 2019-05-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20190505_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcard',
            name='small_description',
            field=models.CharField(max_length=500),
        ),
    ]
