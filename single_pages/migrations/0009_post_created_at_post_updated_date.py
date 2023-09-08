# Generated by Django 4.2.4 on 2023-09-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0008_remove_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]