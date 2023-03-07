# Generated by Django 4.1.5 on 2023-03-01 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('game', '0003_remove_user_games_alter_game_id_alter_game_publisher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.genre')),
            ],
        ),
    ]
