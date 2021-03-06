# Generated by Django 2.1.15 on 2021-01-06 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddDomesticItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('productcost', models.FloatField(blank=True, null=True, verbose_name='Product Cost C$')),
                ('baseproductsalesprice', models.FloatField(blank=True, null=True, verbose_name='Base Product Sales Price C$')),
            ],
            options={
                'verbose_name': 'Domestic Item',
                'verbose_name_plural': 'Domestic Items',
                'db_table': 'tbl_domesticitems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AddImportsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('freight', models.FloatField(blank=True, help_text='Enter the Freight values', null=True, verbose_name='Frieght UNIT')),
                ('freightadmin', models.FloatField(blank=True, help_text='Enter the Freight Admin values', null=True, verbose_name='Frieght Admin/UNIT')),
                ('setupfee', models.FloatField(blank=True, null=True, verbose_name='Setup Fee')),
                ('productcost', models.FloatField(blank=True, null=True, verbose_name='Product Cost U$')),
                ('baseproductsalesprice', models.FloatField(blank=True, null=True, verbose_name='Base Product Sales Price U$')),
                ('totalfrieght', models.FloatField(blank=True, null=True, verbose_name='Total Frieght')),
                ('duty', models.FloatField(blank=True, null=True, verbose_name='Duty (in %)')),
                ('markup', models.FloatField(blank=True, null=True, verbose_name='Markup')),
                ('netduty', models.FloatField(blank=True, null=True, verbose_name='Net Duty U$')),
                ('subtotal', models.FloatField(blank=True, null=True, verbose_name='Sub Total')),
                ('forex', models.FloatField(blank=True, null=True, verbose_name='Forex')),
            ],
            options={
                'verbose_name': 'Imports Item',
                'verbose_name_plural': 'Imports Items',
                'db_table': 'tbl_importsitems',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AdditionalOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=250, null=True)),
                ('optionname', models.CharField(blank=True, max_length=250, null=True)),
                ('optionvalue', models.FloatField(blank=True, null=True)),
                ('markuprate', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark-Up Rate')),
            ],
            options={
                'verbose_name': 'Additional Options',
                'verbose_name_plural': 'Additionals Options',
                'db_table': 'tbl_additionaloption',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'tbl_categories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DomesticProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=250, unique=True)),
                ('productname', models.CharField(max_length=250)),
                ('markup', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark Up Rate(in %)')),
                ('productcostc', models.FloatField(blank=True, default=0.494, null=True, verbose_name='Product Cost C$')),
                ('targetgrossprofit', models.FloatField(blank=True, default=33, null=True, verbose_name='Target Gross Profit (in %)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'Domestic Product',
                'verbose_name_plural': 'Domestic Products',
                'db_table': 'tbl_domesticproducts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ImportsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=250, unique=True)),
                ('productname', models.CharField(max_length=250)),
                ('setupfee', models.IntegerField(blank=True, null=True)),
                ('markuprate', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark Up Rate(in %)')),
                ('targetgrossprofit', models.FloatField(blank=True, null=True, verbose_name='Target Gross Profit (in %)')),
                ('duty', models.IntegerField(blank=True, default=18, null=True, verbose_name='Duty (in %)')),
                ('markup', models.IntegerField(blank=True, default=15, null=True, verbose_name='Markup (in %)')),
                ('frieghtvalue', models.IntegerField(blank=True, default=15, null=True, verbose_name='FRIEGHT ADMIN/UNIT (in %)')),
                ('forex', models.FloatField(blank=True, default=1.35, null=True, verbose_name='Forex')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'Import Product',
                'verbose_name_plural': 'Imports Products',
                'db_table': 'tbl_importproducts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=250, null=True)),
                ('optionname', models.CharField(blank=True, max_length=250, null=True)),
                ('optionvalue', models.FloatField(blank=True, null=True)),
                ('markuprate', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark-Up Rate')),
            ],
            options={
                'verbose_name': 'Products Options',
                'verbose_name_plural': 'Products Options',
                'db_table': 'tbl_productoption',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'db_table': 'tbl_region',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(blank=True, max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region')),
            ],
            options={
                'verbose_name': 'SubCategory',
                'verbose_name_plural': 'SubCategories',
                'db_table': 'tbl_subcategories',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsubcategory', models.CharField(blank=True, max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubCategory')),
            ],
            options={
                'verbose_name': 'SubSubCategory',
                'verbose_name_plural': 'SubSubCategories',
                'db_table': 'tbl_subsubcategories',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='importsproduct',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='importsproduct',
            name='subcatagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubCategory'),
        ),
        migrations.AddField(
            model_name='importsproduct',
            name='subsubcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubSubCategory'),
        ),
        migrations.AddField(
            model_name='domesticproduct',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='domesticproduct',
            name='subcatagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubCategory'),
        ),
        migrations.AddField(
            model_name='domesticproduct',
            name='subsubcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SubSubCategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='addimportsitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ImportsProduct'),
        ),
        migrations.AddField(
            model_name='adddomesticitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DomesticProduct'),
        ),
    ]
