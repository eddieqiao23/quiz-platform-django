# Generated by Django 3.1.6 on 2021-03-20 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='q_statement',
            new_name='question_statement',
        ),
    ]