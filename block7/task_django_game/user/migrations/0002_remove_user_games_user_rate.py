# Generated by Django 4.1.5 on 2023-02-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_remove_user_games_alter_game_id_alter_game_publisher_and_more'),
        ('game_rate', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='games',
        ),
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.ManyToManyField(through='game_rate.GameRate', to='game.game'),
        ),
    ]
