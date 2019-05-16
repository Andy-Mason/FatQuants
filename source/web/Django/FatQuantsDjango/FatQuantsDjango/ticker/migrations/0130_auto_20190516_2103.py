# Generated by Django 2.1.7 on 2019-05-16 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0129_auto_20190516_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='issue_size',
            field=models.FloatField(blank=True, db_column='issue_size', null=True, verbose_name='Issue Size'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='issuer_name',
            field=models.CharField(blank=True, db_column='issuer_name', default='', max_length=100, verbose_name='Issuer Name'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='issuer_type',
            field=models.CharField(blank=True, db_column='issuer_type', default='', max_length=30, verbose_name='Issuer Type'),
        ),
    ]
