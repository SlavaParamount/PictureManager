# Generated by Django 3.2 on 2021-04-14 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managepics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pic',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
