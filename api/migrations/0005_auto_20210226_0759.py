# Generated by Django 3.1.7 on 2021-02-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210226_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='customer',
            new_name='customerID',
        ),
    ]