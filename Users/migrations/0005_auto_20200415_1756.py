# Generated by Django 3.0.4 on 2020-04-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200409_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='firstname',
            field=models.CharField(default=4, max_length=60, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='lastname',
            field=models.CharField(default=3, max_length=60, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='othernames',
            field=models.CharField(default=1, max_length=60, unique=True),
            preserve_default=False,
        ),
    ]