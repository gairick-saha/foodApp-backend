# Generated by Django 2.2.10 on 2020-02-22 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200222_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucard',
            name='items',
        ),
    ]
