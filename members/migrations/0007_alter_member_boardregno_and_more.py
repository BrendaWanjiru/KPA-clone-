# Generated by Django 5.0.5 on 2024-05-16 09:26

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_member_approved_alter_member_boardregno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='BoardRegNo',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='DateRegistration',
            field=models.DateField(null=True, blank=True, default=datetime.date(2024, 4, 24)),
        ),
        migrations.AlterField(
            model_name='member',
            name='PostalCode',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
    ]
