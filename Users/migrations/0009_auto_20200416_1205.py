# Generated by Django 3.0.4 on 2020-04-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20200416_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='othernames',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]