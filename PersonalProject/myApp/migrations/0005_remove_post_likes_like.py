# Generated by Django 4.1.1 on 2022-10-25 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0004_post_likes_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('liked', models.BooleanField(default=False)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Like', to='myApp.post')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-updated',),
            },
        ),
    ]
