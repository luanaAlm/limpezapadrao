# Generated by Django 3.2.4 on 2021-06-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='foto',
            field=models.ImageField(default=1, upload_to='fotos'),
            preserve_default=False,
        ),
    ]
