# Generated by Django 4.2.7 on 2024-11-29 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_blog_tags_event_body_event_desc_event_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img_url',
            field=models.ImageField(upload_to='images/'),
        ),
    ]