# Generated by Django 2.1.3 on 2019-02-13 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0074_auto_20190213_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickerbatchprocesstype',
            name='last_checked',
            field=models.DateTimeField(db_column='last_checked', default=django.utils.timezone.now, verbose_name='Last Checked'),
        ),
    ]
