# Generated by Django 5.0.3 on 2024-03-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_category_book_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pictures',
            field=models.ImageField(default='places/default1.jpg', upload_to='categories_images/'),
        ),
    ]
