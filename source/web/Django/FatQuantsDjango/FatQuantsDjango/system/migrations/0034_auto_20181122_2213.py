# Generated by Django 2.1.3 on 2018-11-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0033_systemauditrecord_field_value_blob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemauditrecord',
            name='field_value_decimal',
            field=models.DecimalField(blank=True, db_column='field_value_decimal', decimal_places=127, max_digits=254, null=True, verbose_name='Decimal'),
        ),
    ]
