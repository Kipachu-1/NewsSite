# Generated by Django 4.1 on 2022-09-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsite', '0021_article_article_url_article_header_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_url',
            field=models.TextField(null=True, unique=True),
        ),
    ]
