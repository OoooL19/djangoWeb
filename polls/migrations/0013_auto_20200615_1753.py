# Generated by Django 3.0.4 on 2020-06-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200612_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='asin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='output',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='output',
            name='price',
            field=models.FloatField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='output',
            name='rank',
            field=models.IntegerField(blank=True, max_length=200),
        ),
    ]
