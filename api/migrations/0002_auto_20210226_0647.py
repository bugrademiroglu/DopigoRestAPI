# Generated by Django 3.1.7 on 2021-02-26 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='amount',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
            preserve_default=False,
        ),
    ]
