# Generated by Django 5.0.1 on 2024-01-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_App', '0002_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='menu_images/'),
        ),
    ]
