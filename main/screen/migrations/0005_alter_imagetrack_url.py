# Generated by Django 4.2.5 on 2024-01-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0004_rename_scalex_imagetrack_scalex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetrack',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
