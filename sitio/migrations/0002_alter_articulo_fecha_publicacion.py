# Generated by Django 3.2.3 on 2021-06-14 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_publicacion',
            field=models.DateField(null=True),
        ),
    ]
