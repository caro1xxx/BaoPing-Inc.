# Generated by Django 3.2.6 on 2023-03-06 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_domain_vote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(default='')),
                ('name', models.CharField(max_length=64)),
                ('count', models.IntegerField(default=0)),
                ('avator', models.FileField(blank=True, upload_to='img')),
                ('vote_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.voteactivity', to_field='vote_id')),
            ],
        ),
    ]