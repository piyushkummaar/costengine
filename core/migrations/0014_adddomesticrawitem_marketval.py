# Generated by Django 2.1.15 on 2021-02-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210217_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddomesticrawitem',
            name='marketval',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Market Value'),
        ),
    ]
