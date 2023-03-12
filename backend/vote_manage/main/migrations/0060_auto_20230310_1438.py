# Generated by Django 3.2.8 on 2023-03-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_voteactivity_track_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_id', models.TextField(default='')),
                ('vote_target_id', models.TextField(default='')),
                ('begin_time', models.IntegerField(default=0)),
                ('end_time', models.IntegerField(default=0)),
                ('day_begin_time', models.IntegerField(default=0)),
                ('space', models.IntegerField(default=0)),
                ('day_count_strict', models.IntegerField(default=0)),
                ('update_time', models.IntegerField(default=0)),
                ('day_vote_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='voteactivity',
            name='officialcount_qrcode',
            field=models.FileField(blank=True, upload_to='pr', verbose_name='公众号二维码'),
        ),
    ]
