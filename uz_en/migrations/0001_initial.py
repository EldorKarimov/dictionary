# Generated by Django 5.0.4 on 2024-04-08 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0002_alter_englishword_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='UzbekWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('word', models.CharField(max_length=50, unique=True, verbose_name='Uzbek word')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.direction')),
            ],
            options={
                'verbose_name': 'Uzbek word',
                'verbose_name_plural': 'Uzbek words',
            },
        ),
        migrations.CreateModel(
            name='EnglishWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('word', models.CharField(max_length=50, verbose_name='english word')),
                ('uzWord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uz_en.uzbekword')),
            ],
            options={
                'verbose_name': 'English word',
                'verbose_name_plural': 'English words',
            },
        ),
    ]