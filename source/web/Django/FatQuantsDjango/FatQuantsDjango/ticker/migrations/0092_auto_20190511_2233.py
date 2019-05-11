# Generated by Django 2.1.7 on 2019-05-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0091_auto_20190511_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='instrument_subtype',
            field=models.CharField(blank=True, choices=[('BASKET', 'Basket'), ('COMPOSITE', 'Composite'), ('CORPORATE', 'Corporate Bond'), ('ETC', 'Exchange-Traded Commodity'), ('ETF', 'Exchange-Traded Fund'), ('ETN', 'Exchange-Traded Note'), ('FORWARD', 'Forward'), ('GDR', 'Global Depositary Receipt'), ('GOVERNMENT', 'Government Bond'), ('MARKET', 'Market Index'), ('OEIC', 'Open-Ended Investment Company'), ('ORDINARY', 'Ordinary Share'), ('PREFERENCE', 'Preference Share'), ('REGIONAL', 'Regional Index'), ('SECTOR', 'Sector Index'), ('SICAV', 'SICAV'), ('SPOT', 'Spot'), ('SUPRANATIONAL', 'Supranational Bond'), ('UT', 'Unit Trust'), ('WARRANT', 'Warrant')], db_column='instrument_subtype', default='', max_length=30, verbose_name='Instrument Subtype'),
        ),
    ]
