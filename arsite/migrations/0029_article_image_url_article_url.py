# Generated by Django 4.1 on 2022-09-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsite', '0028_remove_article_image_url_remove_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.TextField(null=True, unique=True),
        ),
    ]