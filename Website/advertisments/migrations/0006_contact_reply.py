# Generated by Django 3.0.7 on 2020-07-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisments', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='reply',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
