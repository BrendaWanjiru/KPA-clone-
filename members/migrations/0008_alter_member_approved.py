# Generated by Django 5.0.5 on 2024-05-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_member_boardregno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Approved',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
    ]