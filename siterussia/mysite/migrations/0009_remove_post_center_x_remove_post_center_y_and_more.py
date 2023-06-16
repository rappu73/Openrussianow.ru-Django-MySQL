# Generated by Django 4.2.1 on 2023-05-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_post_center_x_alter_post_center_y'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='center_x',
        ),
        migrations.RemoveField(
            model_name='post',
            name='center_y',
        ),
        migrations.AddField(
            model_name='post',
            name='center',
            field=models.CharField(max_length=255, null=True, verbose_name='Координата'),
        ),
    ]