# Generated by Django 3.2.6 on 2023-03-06 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20230306_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterecord',
            name='vote_target',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.votetarget'),
            preserve_default=False,
        ),
    ]