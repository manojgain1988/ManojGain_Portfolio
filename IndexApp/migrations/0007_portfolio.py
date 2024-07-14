# Generated by Django 5.0.7 on 2024-07-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndexApp', '0006_remove_service_image_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='portfolio/')),
                ('title', models.CharField(blank=True, max_length=700)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]