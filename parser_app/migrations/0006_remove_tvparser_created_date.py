# Generated by Django 4.1.7 on 2023-03-02 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0005_remove_tvparser_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvparser',
            name='created_date',
        ),
    ]
