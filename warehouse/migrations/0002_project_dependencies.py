# Generated by Django 2.2 on 2019-04-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dependencies',
            field=models.TextField(default='[]'),
            preserve_default=False,
        ),
    ]
