# Generated by Django 4.1.1 on 2022-10-25 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0002_alter_like_post_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
