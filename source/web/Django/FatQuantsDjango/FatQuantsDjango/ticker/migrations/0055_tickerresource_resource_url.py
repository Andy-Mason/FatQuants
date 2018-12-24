# Generated by Django 2.1.3 on 2018-12-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0054_auto_20181224_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickerresource',
            name='resource_url',
            field=models.URLField(db_column='resource_url', default='', max_length=2000, verbose_name='Resource URL'),
        ),
    ]