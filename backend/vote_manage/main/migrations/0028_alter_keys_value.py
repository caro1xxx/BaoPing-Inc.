# Generated by Django 3.2.6 on 2023-03-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_keys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keys',
            name='value',
            field=models.CharField(db_index=True, default='', max_length=128),
        ),
    ]
