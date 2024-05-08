# Generated by Django 5.0.3 on 2024-05-08 07:06

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_category_tag_remove_poem_language_remove_poem_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='poem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='accounts.poem'),
        ),
    ]
