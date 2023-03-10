# Generated by Django 4.1.7 on 2023-03-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_customuser_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_food',
            field=models.CharField(max_length=20, null=True, verbose_name='любимая еда'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_sport',
            field=models.CharField(max_length=20, null=True, verbose_name='любимый спорт'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.CharField(max_length=20, null=True, verbose_name='рост'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='hobby',
            field=models.CharField(max_length=20, null=True, verbose_name='хобби'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.CharField(max_length=20, null=True, verbose_name='вес'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education',
            field=models.CharField(choices=[(1, 'HIGHER'), (2, 'AVERAGE')], max_length=20, null=True),
        ),
    ]
