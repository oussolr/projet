# Generated by Django 2.0.3 on 2018-04-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage_propose',
            name='Durée',
            field=models.DurationField(),
        ),
    ]
