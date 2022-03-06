# Generated by Django 4.0.3 on 2022-03-06 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_remove_subjects_staff_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='subject_code',
        ),
        migrations.AddField(
            model_name='subjects',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
