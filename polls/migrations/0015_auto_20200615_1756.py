# Generated by Django 3.0.4 on 2020-06-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20200615_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='price',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
    ]
