# Generated by Django 4.0.3 on 2022-04-11 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_tag_post_tags'),
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
