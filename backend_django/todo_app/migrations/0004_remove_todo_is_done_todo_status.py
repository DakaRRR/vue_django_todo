# Generated by Django 4.1.3 on 2022-11-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_rename_done_todo_is_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='is_done',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('todo', 'Todo'), ('done', 'Done')], default='todo', max_length=10),
        ),
    ]
