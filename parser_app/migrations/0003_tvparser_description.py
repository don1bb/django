# Generated by Django 4.1.7 on 2023-03-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0002_remove_tvparser_description_remove_tvparser_prise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvparser',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
