# Generated by Django 4.2.6 on 2023-12-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_author_category_publisher_alter_news_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='publishers',
            field=models.ManyToManyField(to='app.publisher'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]