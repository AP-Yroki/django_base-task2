# Generated by Django 4.2.6 on 2023-12-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_news_author_news_category_news_publishers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='authors',
            field=models.ManyToManyField(to='app.author'),
        ),
    ]
