# Generated by Django 4.1 on 2022-09-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsite', '0015_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Author',
            field=models.CharField(max_length=100),
        ),
    ]
