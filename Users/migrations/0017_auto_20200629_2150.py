# Generated by Django 3.0.4 on 2020-06-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_auto_20200623_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='referral_code',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
    ]
