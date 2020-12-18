# Generated by Django 2.2.13 on 2020-07-17 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_position', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('file_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=15, null=True, unique=True)),
                ('phone_number_confirmed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'active'), ('disabled', 'disabled'), ('archived', 'archived'), ('deleted', 'deleted')], max_length=10)),
                ('is_resource', models.BooleanField(default=False)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('date_terminated', models.DateField(blank=True, null=True)),
                ('src_resource_id', models.CharField(blank=True, max_length=40, null=True)),
                ('job_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_position.JobPosition')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.Organization')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
