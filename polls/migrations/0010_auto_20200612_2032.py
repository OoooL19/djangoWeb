# Generated by Django 3.0.4 on 2020-06-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200612_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='rank',
            field=models.FloatField(max_length=200),
        ),
    ]
