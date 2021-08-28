# Generated by Django 3.2.6 on 2021-08-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_cap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketcap',
            name='coin_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='coin code'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='coin_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='coin name'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='d7',
            field=models.FloatField(blank=True, null=True, verbose_name='d7'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='h1',
            field=models.FloatField(blank=True, null=True, verbose_name='h1'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='h24',
            field=models.FloatField(blank=True, null=True, verbose_name='h24'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='h24_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='h24'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='info_url',
            field=models.CharField(blank=True, max_length=2083, null=True, verbose_name='info url'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='market_cap',
            field=models.FloatField(blank=True, null=True, verbose_name='market'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='marketcap',
            name='sparkline_url',
            field=models.CharField(blank=True, max_length=2083, null=True, verbose_name='sparkline url'),
        ),
    ]
