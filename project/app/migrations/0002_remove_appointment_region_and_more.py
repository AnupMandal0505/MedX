# Generated by Django 4.2.5 on 2023-09-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='region',
        ),
        migrations.AddField(
            model_name='appointment',
            name='predicted_diagnosis',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]