# Generated by Django 5.0.5 on 2024-05-17 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0019_alter_member_dateregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='MemberNo',
            new_name='MemberID',
        ),
    ]