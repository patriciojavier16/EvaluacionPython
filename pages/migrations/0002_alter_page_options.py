# Generated by Django 4.2.4 on 2023-09-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['created'], 'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
    ]
