# Generated by Django 5.1.4 on 2024-12-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
