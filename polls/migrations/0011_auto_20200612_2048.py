# Generated by Django 3.0.4 on 2020-06-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200612_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='rank',
            field=models.CharField(max_length=200),
        ),
    ]