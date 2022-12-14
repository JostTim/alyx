# Generated by Django 3.2.4 on 2021-07-01 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0010_auto_20210624_1253'),
        ('misc', '0008_auto_20210624_1253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0015_auto_20210624_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicRecording',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', models.JSONField(blank=True, help_text='Structured data, formatted in a user-defined way', null=True)),
                ('narrative', models.TextField(blank=True)),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='misc.lab')),
                ('location', models.ForeignKey(blank=True, help_text='The physical location at which the action was performed', null=True, on_delete=django.db.models.deletion.SET_NULL, to='misc.lablocation')),
                ('procedures', models.ManyToManyField(blank=True, help_text='The procedure(s) performed', to='actions.ProcedureType')),
                ('subject', models.ForeignKey(help_text='The subject on which this action was performed', on_delete=django.db.models.deletion.CASCADE, related_name='actions_chronicrecordings', to='subjects.subject')),
                ('users', models.ManyToManyField(blank=True, help_text='The user(s) involved in this action', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
