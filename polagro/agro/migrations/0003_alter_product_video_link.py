# Generated by Django 4.0.2 on 2022-02-19 17:24

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0002_alter_product_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video_link',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
