# Generated by Django 4.0.2 on 2022-02-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video_link',
            field=models.URLField(max_length=50),
        ),
    ]