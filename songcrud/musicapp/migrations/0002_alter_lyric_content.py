# Generated by Django 4.1.2 on 2022-10-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
