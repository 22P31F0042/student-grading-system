# Generated by Django 3.2 on 2023-11-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_gradesystem_s_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradesystem',
            name='course',
            field=models.CharField(default='no', max_length=200),
        ),
    ]
