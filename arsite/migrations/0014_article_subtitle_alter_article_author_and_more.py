# Generated by Django 4.1 on 2022-09-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsite', '0013_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='Author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
