# Generated by Django 3.2.6 on 2023-03-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_voteactivity_vote_voteusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_income', models.IntegerField(default=0)),
                ('yesterday_income', models.IntegerField(default=0)),
                ('today_order_count', models.IntegerField(default=0)),
                ('yesterday_order_count', models.IntegerField(default=0)),
                ('now_month_income', models.IntegerField(default=0)),
                ('create_time', models.IntegerField(default=0)),
            ],
        ),
    ]
