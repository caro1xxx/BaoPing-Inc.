# Generated by Django 3.2.8 on 2023-03-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_paymentrecord_support_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statics',
            name='today_income',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='statics',
            name='yesterday_income',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='staticshistory',
            name='day_income',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='staticshistory',
            name='day_time',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]