# Generated by Django 4.2.1 on 2023-06-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_alter_post_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentnew',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]