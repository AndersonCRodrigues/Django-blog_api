# Generated by Django 4.2 on 2023-04-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('blog_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]