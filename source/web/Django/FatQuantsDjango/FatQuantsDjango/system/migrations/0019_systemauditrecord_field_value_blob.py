# Generated by Django 2.1.3 on 2018-11-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0018_systemauditrecord_field_value_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_blob',
            field=models.BinaryField(blank=True, db_column='field_value_blob', null=True, verbose_name='BLOB'),
        ),
    ]