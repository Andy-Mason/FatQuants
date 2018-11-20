# Generated by Django 2.1.3 on 2018-11-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0013_testdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdata',
            name='description',
            field=models.CharField(db_column='description', default='', max_length=250, unique=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='testdata',
            name='notes',
            field=models.CharField(blank=True, db_column='notes', max_length=1000, null=True, verbose_name='Notes'),
        ),
    ]
