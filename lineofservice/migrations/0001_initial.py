# Generated by Django 2.2.13 on 2020-07-17 22:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineOfService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('src_los_id', models.UUIDField(blank=True, null=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.Organization')),
            ],
            options={
                'verbose_name_plural': 'Lines of Service',
                'db_table': 'line_of_service',
            },
        ),
    ]