# Generated by Django 3.2.8 on 2021-10-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_automovel_cama_tapete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('ID_Depoimento', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('foto', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('ID_Parceiro', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('foto', models.URLField()),
            ],
        ),
    ]