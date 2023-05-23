# Generated by Django 4.2 on 2023-04-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=100)),
                ('buy_rate', models.CharField(max_length=20)),
                ('sell_rate', models.CharField(max_length=20)),
                ('buy_active', models.BooleanField(default=True)),
                ('sell_active', models.BooleanField(default=True)),
                ('logo', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100)),
                ('buy_rate', models.CharField(max_length=20)),
                ('sell_rate', models.CharField(max_length=20)),
                ('buy_active', models.BooleanField(default=True)),
                ('sell_active', models.BooleanField(default=True)),
                ('logo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]