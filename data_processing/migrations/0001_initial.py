# Generated by Django 5.1.3 on 2024-11-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TickerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.BigIntegerField()),
                ('atr', models.FloatField(blank=True, null=True)),
                ('buy_signal', models.BooleanField(default=False)),
                ('sell_signal', models.BooleanField(default=False)),
            ],
        ),
    ]
