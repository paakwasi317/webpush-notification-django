# Generated by Django 3.0.4 on 2020-04-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20200419_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='images/userlogo/'),
        ),
    ]