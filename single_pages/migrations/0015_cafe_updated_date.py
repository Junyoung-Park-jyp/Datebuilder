# Generated by Django 4.2.4 on 2023-09-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0014_merge_20230911_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
