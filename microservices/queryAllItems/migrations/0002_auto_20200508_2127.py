# Generated by Django 3.0.6 on 2020-05-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queryAllItems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BazaarOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('ordersNum', models.IntegerField()),
                ('pricePerUnit', models.FloatField()),
                ('sell_or_buy', models.BooleanField()),
                ('item_id', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='bazaar_orders',
        ),
    ]
