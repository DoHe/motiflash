# Generated by Django 3.1.7 on 2021-04-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='a', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]