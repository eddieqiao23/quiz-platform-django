# Generated by Django 3.1.6 on 2021-05-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_quiz_max_subs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_statement',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='submission',
            name='sub_answer',
            field=models.CharField(default='', max_length=250),
        ),
    ]