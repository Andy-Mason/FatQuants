# Generated by Django 2.1.3 on 2019-02-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JsonData',
            fields=[
                ('json_data_id', models.BigAutoField(db_column='json_data_id', primary_key=True, serialize=False, verbose_name='JsonDataID')),
            ],
            options={
                'db_table': 'json_data',
            },
        ),
    ]