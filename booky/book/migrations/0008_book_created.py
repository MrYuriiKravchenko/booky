# Generated by Django 4.2 on 2024-08-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_publishing_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2024-08-26 12:00:00'),
            preserve_default=False,
        ),
    ]
