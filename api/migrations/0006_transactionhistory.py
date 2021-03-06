# Generated by Django 3.1.7 on 2021-02-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210226_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField()),
                ('senderAcountID', models.CharField(max_length=100)),
                ('receiverAcountID', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
