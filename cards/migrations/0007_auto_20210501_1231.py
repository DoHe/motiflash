# Generated by Django 3.2 on 2021-05-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_profile_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]