# Generated by Django 3.2 on 2023-11-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0006_gradesystem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradesystem',
            name='ML_marks',
            field=models.IntegerField(default=0),
        ),
    ]
