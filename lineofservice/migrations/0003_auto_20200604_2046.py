# Generated by Django 2.2.12 on 2020-06-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lineofservice', '0002_lineofservice_src_los_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineofservice',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lineofservice',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
