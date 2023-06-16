# Generated by Django 4.2.1 on 2023-05-29 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото2'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото3'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото4'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото5'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysite.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото1'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]