# Generated by Django 4.0.3 on 2022-04-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_category_slug_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=5000, verbose_name='Описание'),
        ),
    ]
