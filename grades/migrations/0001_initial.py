# Generated by Django 3.2 on 2023-11-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gradesystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ml_marks', models.IntegerField(max_length=100)),
                ('web_marks', models.IntegerField(max_length=100)),
                ('iot_marks', models.IntegerField(max_length=100)),
                ('cns_marks', models.IntegerField(max_length=100)),
                ('spm_marks', models.IntegerField(max_length=100)),
            ],
        ),
    ]
