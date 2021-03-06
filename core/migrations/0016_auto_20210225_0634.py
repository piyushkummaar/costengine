# Generated by Django 2.1.15 on 2021-02-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210225_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='distributor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Distributor $$'),
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='distributorcost',
            field=models.DecimalField(blank=True, decimal_places=9, max_digits=9, null=True, verbose_name='Disributor Cost'),
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='distributormargin',
            field=models.IntegerField(default=[], verbose_name='Distributor Margin(in %)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='listprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='List price'),
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='marginonsell',
            field=models.IntegerField(default=[], verbose_name='Margin On Sell'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='markup',
            field=models.IntegerField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='netsellprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Net Sell Price'),
        ),
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='onnetsell',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='$$ On Net Sell Price'),
        ),
    ]
