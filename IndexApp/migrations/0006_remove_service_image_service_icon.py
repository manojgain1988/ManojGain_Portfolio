# Generated by Django 5.0.7 on 2024-07-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndexApp', '0005_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
