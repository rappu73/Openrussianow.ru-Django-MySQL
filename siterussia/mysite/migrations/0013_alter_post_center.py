# Generated by Django 4.2.1 on 2023-06-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_commentnew_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='center',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Координата'),
        ),
    ]