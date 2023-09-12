# Generated by Django 4.2.4 on 2023-09-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0003_course_cafe_course_food_course_place_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='single_pages/files/cafe/'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='single_pages/images/cafe/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='single_pages/files/food/'),
        ),
        migrations.AlterField(
            model_name='food',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='single_pages/images/food/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='file_upload',
            field=models.FileField(blank=True, null=True, upload_to='single_pages/files/place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='head_image',
            field=models.ImageField(blank=True, null=True, upload_to='single_pages/images/place/'),
        ),
    ]
