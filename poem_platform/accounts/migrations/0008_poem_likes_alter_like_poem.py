# Generated by Django 5.0.3 on 2024-05-08 09:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customuser_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_poems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='poem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to='accounts.poem'),
        ),
    ]
