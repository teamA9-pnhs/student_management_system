# Generated by Django 4.0.3 on 2022-03-05 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_remove_subjects_course_id_subjects_credits_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='semester',
        ),
    ]
