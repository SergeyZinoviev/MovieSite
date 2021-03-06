# Generated by Django 4.0.3 on 2022-05-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_alter_post_actors_alter_post_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='actors',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Актеры'),
        ),
        migrations.AlterField(
            model_name='post',
            name='director',
            field=models.CharField(blank=True, max_length=50, verbose_name='Режиссер'),
        ),
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='post',
            name='quality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movie.quality', verbose_name='Качество'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rateIMDB',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Рейтинг IMDB'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rateKP',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Рейтинг КП'),
        ),
        migrations.AlterField(
            model_name='post',
            name='released',
            field=models.CharField(blank=True, max_length=15, verbose_name='Год выхода'),
        ),
        migrations.AlterField(
            model_name='post',
            name='side',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='post',
            name='translation',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Перевод'),
        ),
    ]
