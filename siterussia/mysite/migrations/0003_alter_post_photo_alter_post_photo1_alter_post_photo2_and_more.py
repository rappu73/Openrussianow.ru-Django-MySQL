# Generated by Django 4.2.1 on 2023-05-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_post_photo1_post_photo2_post_photo3_post_photo4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, height_field=500, upload_to='photos', verbose_name='Фото1', width_field=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, height_field=500, upload_to='photos', verbose_name='Фото2', width_field=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, height_field=500, upload_to='photos', verbose_name='Фото3', width_field=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, height_field=500, upload_to='photos', verbose_name='Фото4', width_field=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, height_field=500, upload_to='photos', verbose_name='Фото5', width_field=500),
        ),
    ]