# Generated by Django 4.1.2 on 2023-04-17 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_with_image_excerpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_with_image',
            old_name='tags_for_seo',
            new_name='tags_for_seo_and_search_bar_in_website',
        ),
    ]
