# Generated by Django 3.0.3 on 2020-04-07 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200401_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
