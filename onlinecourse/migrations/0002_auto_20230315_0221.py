# Generated by Django 3.1.3 on 2023-03-15 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='courses',
            new_name='course',
        ),
    ]
