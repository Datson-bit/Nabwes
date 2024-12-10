# Generated by Django 4.2.7 on 2024-11-29 21:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_blogs_blog_rename_events_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.AddField(
            model_name='event',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='blog',
            name='authour_img',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='images',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
