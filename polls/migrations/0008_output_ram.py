# Generated by Django 3.0.4 on 2020-06-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_output_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='ram',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
