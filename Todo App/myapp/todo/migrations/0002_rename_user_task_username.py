# Generated by Django 4.2.6 on 2024-03-21 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='username',
        ),
    ]
