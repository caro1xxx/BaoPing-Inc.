# Generated by Django 3.2.8 on 2023-03-14 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_alter_voteactivity_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecord',
            name='vote_target',
            field=models.IntegerField(default=0),
        ),
    ]
