# Generated by Django 4.0.2 on 2022-02-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0004_rename_video_link_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('seed', 'SEED AND PLANT'), ('fertilizers', 'FERTILIZERS'), ('traps', 'TRAPS'), ('pesticedes', 'PESTICIDES')], default='green', max_length=20),
        ),
    ]
