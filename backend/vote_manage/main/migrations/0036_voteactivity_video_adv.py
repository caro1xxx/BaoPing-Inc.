# Generated by Django 3.2.8 on 2023-03-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_voteactivity_bottom_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteactivity',
            name='video_adv',
            field=models.FileField(blank=True, upload_to='img', verbose_name='视频广告'),
        ),
    ]
