# Generated by Django 5.0.5 on 2024-05-13 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_members_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='position',
        ),
    ]
