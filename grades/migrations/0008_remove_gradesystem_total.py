# Generated by Django 3.2 on 2023-12-01 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0007_alter_gradesystem_ml_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradesystem',
            name='total',
        ),
    ]
