# Generated by Django 4.2.4 on 2023-09-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0005_delete_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='play',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
