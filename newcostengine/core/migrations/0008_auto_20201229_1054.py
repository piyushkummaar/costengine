# Generated by Django 3.1.4 on 2020-12-29 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201229_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addimportsitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.importsproduct'),
        ),
    ]
