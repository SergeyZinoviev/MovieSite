# Generated by Django 4.0.3 on 2022-04-11 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_category_slug_remove_post_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
