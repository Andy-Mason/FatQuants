# Generated by Django 2.1.3 on 2018-11-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_systemauditrecord_field_value_boolean'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_integer',
            field=models.BigIntegerField(blank=True, db_column='field_value_integer', null=True, verbose_name='Integer'),
        ),
    ]
