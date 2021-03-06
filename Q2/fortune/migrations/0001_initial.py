# Generated by Django 3.1 on 2020-10-10 10:19

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
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.company')),
            ],
        ),
        migrations.CreateModel(
            name='FoodPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_option', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0.0)),
                ('status', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.company')),
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
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('foodpackage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.foodpackage')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.order')),
            ],
        ),
        migrations.CreateModel(
            name='FortuneCookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fortune_option', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.company')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fortune.company')),
            ],
        ),
    ]
