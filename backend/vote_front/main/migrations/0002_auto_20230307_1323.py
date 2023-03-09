# Generated by Django 3.2.6 on 2023-03-07 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteactivity',
            name='contact',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='voteactivity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='voteactivity',
            name='enterprises',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='voteactivity',
            name='prize',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='voteactivity',
            name='support',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='voteactivity',
            name='vote_id',
            field=models.IntegerField(db_index=True, unique=True),
        ),
        migrations.CreateModel(
            name='keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_index=True, default='', max_length=128)),
                ('expire_time', models.IntegerField(default=0)),
                ('has_used', models.IntegerField(default=0)),
                ('user_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.voteuser', to_field='open_id')),
            ],
        ),
    ]