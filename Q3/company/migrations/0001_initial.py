# Generated by Django 3.1 on 2020-10-09 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('gst_number', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_phone', models.CharField(max_length=30)),
                ('customer_email', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total_role', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('total_cost', models.FloatField()),
                ('discount', models.FloatField()),
                ('final_cost', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('order_cost', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_width', models.FloatField()),
                ('item_length', models.FloatField()),
                ('item_cost', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.item')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_width', models.FloatField()),
                ('item_length', models.FloatField()),
                ('mrp', models.FloatField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.order')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_width', models.FloatField()),
                ('role_length', models.FloatField()),
                ('status', models.BooleanField(default=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_item_width', models.FloatField()),
                ('available_item_length', models.FloatField()),
                ('colour', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.itemcategory'),
        ),
    ]