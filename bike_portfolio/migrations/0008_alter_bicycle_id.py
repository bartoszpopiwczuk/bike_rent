# Generated by Django 5.1.3 on 2024-12-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_portfolio', '0007_alter_bicycle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
