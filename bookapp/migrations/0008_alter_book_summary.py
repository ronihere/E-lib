# Generated by Django 3.2.5 on 2022-04-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_alter_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=230),
        ),
    ]
