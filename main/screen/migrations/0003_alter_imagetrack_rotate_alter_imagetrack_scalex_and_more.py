# Generated by Django 4.2.5 on 2024-01-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_imagetrack_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetrack',
            name='rotate',
            field=models.DecimalField(decimal_places=20, max_digits=30),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='scalex',
            field=models.DecimalField(decimal_places=20, max_digits=30),
        ),
        migrations.AlterField(
            model_name='imagetrack',
            name='scaley',
            field=models.DecimalField(decimal_places=20, max_digits=30),
        ),
    ]