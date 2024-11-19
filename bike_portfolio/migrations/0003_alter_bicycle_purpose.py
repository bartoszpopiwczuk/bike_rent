# Generated by Django 5.1.3 on 2024-11-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_portfolio', '0002_rename_type_bicycle_purpose_bicycle_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='purpose',
            field=models.CharField(choices=[('mtb', 'Mountain'), ('road', 'Road'), ('gravel', 'Gravel'), ('city', 'City')], max_length=30),
        ),
    ]
