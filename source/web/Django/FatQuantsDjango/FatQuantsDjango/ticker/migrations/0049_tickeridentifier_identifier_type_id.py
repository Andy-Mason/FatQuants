# Generated by Django 2.1.3 on 2018-12-24 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0037_productprovider'),
        ('ticker', '0048_tickeridentifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickeridentifier',
            name='identifier_type_id',
            field=models.ForeignKey(db_column='identifier_type_id', default=0, on_delete=django.db.models.deletion.PROTECT, to='reference_data.IdentifierType', verbose_name='Identifier Type'),
        ),
    ]
