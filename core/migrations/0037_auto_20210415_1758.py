# Generated by Django 2.2 on 2021-04-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_adddomesticsizeitem_domesticsizeproduct_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddomesticsizeitem',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='core.Size'),
        ),
    ]
