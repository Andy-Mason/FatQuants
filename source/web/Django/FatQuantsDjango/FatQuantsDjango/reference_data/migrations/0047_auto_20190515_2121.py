# Generated by Django 2.1.7 on 2019-05-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0046_instrumenttype_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiertype',
            name='identifier_type',
            field=models.CharField(db_column='identifier_type', default='', max_length=20, unique=True, verbose_name='IdentifierType'),
        ),
    ]
