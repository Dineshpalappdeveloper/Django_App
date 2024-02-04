# Generated by Django 5.0.1 on 2024-02-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gshop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chassisnumber',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
