# Generated by Django 3.1.5 on 2021-01-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content_rating',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='design_rating',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability_rating',
            field=models.FloatField(default=1),
        ),
    ]
