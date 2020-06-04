# Generated by Django 2.2.12 on 2020-06-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
