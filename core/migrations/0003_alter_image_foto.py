# Generated by Django 3.2.4 on 2021-06-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_image_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='foto',
            field=models.ImageField(upload_to='fotos/%y'),
        ),
    ]
