# Generated by Django 5.0.4 on 2024-05-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_alter_about_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='share',
            field=models.URLField(default='', verbose_name='URL'),
            preserve_default=False,
        ),
    ]
