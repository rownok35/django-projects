# Generated by Django 3.2.4 on 2021-06-05 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=264, verbose_name='Put a Title')),
                ('slug', models.SlugField(max_length=264, unique=True)),
                ('article_content', models.TextField(verbose_name='What is on your mind?')),
                ('article_image', models.ImageField(upload_to='article_images', verbose_name='Image')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('update_data', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish_date',),
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_article', to='Article.article_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='Article.article_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-comment_date',),
            },
        ),
    ]