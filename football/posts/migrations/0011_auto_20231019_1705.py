# Generated by Django 2.2.19 on 2023-10-19 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20231019_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Tournament'),
        ),
    ]
