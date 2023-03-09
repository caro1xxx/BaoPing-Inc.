# Generated by Django 3.2.8 on 2023-03-09 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_delete_commentrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('create_time', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('vote_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.votetarget')),
                ('vote_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.voteuser', to_field='open_id')),
            ],
        ),
    ]
