# Generated by Django 4.2.7 on 2024-12-10 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_executives'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parliamentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='gallery_images/')),
                ('facebook_link', models.CharField(max_length=2000)),
                ('linkedIn_link', models.CharField(max_length=2000)),
                ('twitter_link', models.CharField(max_length=2000)),
            ],
        ),
    ]