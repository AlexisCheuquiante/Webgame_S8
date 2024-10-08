# Generated by Django 5.1 on 2024-09-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_juego'),
    ]

    operations = [
        migrations.CreateModel(
            name='aventura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_juego', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_juego', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estrategia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_juego', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Infantiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_juego', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='juego',
            old_name='Descripcion',
            new_name='descripcion_juego',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='Id_juego',
        ),
    ]
