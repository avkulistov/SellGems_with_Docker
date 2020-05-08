# Generated by Django 3.0.6 on 2020-05-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=64, verbose_name='Customer')),
                ('item', models.CharField(max_length=64, verbose_name='Item')),
                ('total', models.FloatField(verbose_name='total')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
        ),
    ]