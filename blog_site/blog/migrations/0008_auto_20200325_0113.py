# Generated by Django 3.0.3 on 2020-03-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200324_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]