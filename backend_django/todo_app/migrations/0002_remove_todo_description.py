# Generated by Django 4.1.3 on 2022-11-01 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]