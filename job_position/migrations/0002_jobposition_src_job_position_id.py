# Generated by Django 2.2.5 on 2019-10-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_position', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposition',
            name='src_job_position_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
