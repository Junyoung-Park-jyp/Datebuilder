# Generated by Django 4.2.4 on 2023-09-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0006_cafe_updated_date_alter_cafe_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_at', models.TextField()),
            ],
        ),
    ]
