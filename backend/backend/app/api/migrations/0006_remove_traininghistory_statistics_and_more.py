# Generated by Django 4.0.2 on 2022-02-13 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_exercise_body_part_alter_exercise_imagepath_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traininghistory',
            name='statistics',
        ),
        migrations.AddField(
            model_name='traininghistory',
            name='statistics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='stat_name', to='api.statistics'),
        ),
    ]
