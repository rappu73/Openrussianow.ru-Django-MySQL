# Generated by Django 4.2.1 on 2023-06-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_post_scale'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.TextField(blank=True, null=True, verbose_name='Видео по теме'),
        ),
    ]