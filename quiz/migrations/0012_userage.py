# Generated by Django 3.1.6 on 2021-06-02 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quiz', '0011_auto_20210601_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAge',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
