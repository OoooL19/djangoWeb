# Generated by Django 3.0.4 on 2020-06-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200611_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='cpu',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]