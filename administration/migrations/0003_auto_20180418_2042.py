# Generated by Django 2.0.3 on 2018-04-18 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_auto_20180418_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adresse',
            name='Etudiant',
            field=models.ForeignKey(default='-1', limit_choices_to='3', on_delete=django.db.models.deletion.CASCADE, to='administration.Etudiant'),
        ),
    ]