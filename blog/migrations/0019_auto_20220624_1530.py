# Generated by Django 3.2.9 on 2022-06-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
