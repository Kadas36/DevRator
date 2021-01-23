# Generated by Django 3.1.5 on 2021-01-23 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('design_rating', models.FloatField(default=0)),
                ('usability_rating', models.FloatField(default=0)),
                ('content_rating', models.FloatField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.project')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.profile')),
            ],
        ),
    ]
