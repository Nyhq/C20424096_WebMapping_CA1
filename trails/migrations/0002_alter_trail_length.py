# Generated by Django 4.2.6 on 2023-11-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='length',
            field=models.FloatField(editable=False),
        ),
    ]
