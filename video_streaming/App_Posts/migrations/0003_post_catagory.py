# Generated by Django 3.1.7 on 2021-06-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Posts', '0002_dislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.CharField(choices=[('Music', 'Music'), ('Science', 'Science'), ('Sports', 'Sports'), ('Game', 'Game'), ('Dance', 'Dance'), ('Others', 'Others')], default='Others', max_length=264),
        ),
    ]