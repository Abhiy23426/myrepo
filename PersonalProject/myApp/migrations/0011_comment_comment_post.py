# Generated by Django 4.1.1 on 2022-10-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_alter_like_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_post',
            field=models.BooleanField(default=True),
        ),
    ]
