# Generated by Django 3.0.6 on 2020-05-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/%d/%m/%Y/'),
        ),
    ]