# Generated by Django 2.1.3 on 2018-11-22 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0030_auto_20181122_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_text',
            field=models.TextField(blank=True, db_column='field_value_text', null=True, verbose_name='Text'),
        ),
    ]
