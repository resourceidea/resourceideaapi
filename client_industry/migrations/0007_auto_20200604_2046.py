# Generated by Django 2.2.12 on 2020-06-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_industry', '0006_auto_20190925_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientindustry',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clientindustry',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
