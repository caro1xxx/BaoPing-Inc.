# Generated by Django 3.2.6 on 2023-03-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_voteactivity_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteactivity',
            name='enable_browser',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='voteactivity',
            name='enable_prize',
            field=models.IntegerField(default=1),
        ),
    ]
