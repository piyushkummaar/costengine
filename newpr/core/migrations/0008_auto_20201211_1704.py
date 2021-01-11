# Generated by Django 3.1.4 on 2020-12-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201210_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcost',
            name='get_prduct_cost',
            field=models.ManyToManyField(to='core.Price'),
        ),
        migrations.RemoveField(
            model_name='productcost',
            name='prduct_cost',
        ),
        migrations.AddField(
            model_name='productcost',
            name='prduct_cost',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
