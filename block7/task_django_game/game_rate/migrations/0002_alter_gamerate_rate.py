# Generated by Django 4.1.5 on 2023-03-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_rate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerate',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
