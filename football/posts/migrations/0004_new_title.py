# Generated by Django 2.2.19 on 2023-10-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='title',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
    ]
