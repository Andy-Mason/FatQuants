# Generated by Django 2.1.3 on 2018-11-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0007_identifiertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='identifiertype',
            name='description',
            field=models.CharField(db_column='description', default='', max_length=250, unique=True, verbose_name='Description'),
        ),
    ]