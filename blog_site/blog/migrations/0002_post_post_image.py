# Generated by Django 3.0.3 on 2020-03-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
