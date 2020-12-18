# Generated by Django 2.2.13 on 2020-07-17 22:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('name_slug', models.CharField(editable=False, max_length=256, unique=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('disabled', 'disabled'), ('archived', 'archived'), ('deleted', 'deleted')], max_length=10)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
    ]
