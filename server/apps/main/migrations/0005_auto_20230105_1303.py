# Generated by Django 2.2.17 on 2023-01-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_update_publicexperience_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicexperience',
            name='id',
        ),
        migrations.AlterField(
            model_name='publicexperience',
            name='experience_id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]