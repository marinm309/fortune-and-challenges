# Generated by Django 4.0 on 2023-01-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_customer_is_wheel_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_wheel_spin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
