# Generated by Django 4.1.1 on 2022-09-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='urgente',
            field=models.BooleanField(default=False),
        ),
    ]
