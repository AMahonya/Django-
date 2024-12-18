# Generated by Django 4.2.17 on 2024-12-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_game_cost_alter_game_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок новости', max_length=100)),
                ('content', models.TextField(help_text='Содержание новости')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Дата публикации')),
            ],
        ),
    ]
