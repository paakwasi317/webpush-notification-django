# Generated by Django 3.0.4 on 2020-04-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20200415_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='firstname',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastname',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='users',
            name='othernames',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=60),
        ),
    ]
