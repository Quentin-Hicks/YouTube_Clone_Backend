# Generated by Django 4.0.3 on 2022-03-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
