# Generated by Django 3.1.6 on 2021-03-22 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_question_solution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='content',
            new_name='name',
        ),
    ]