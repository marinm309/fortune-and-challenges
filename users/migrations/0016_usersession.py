# Generated by Django 4.0 on 2023-01-03 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('users', '0015_alter_customer_last_wheel_spin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.appuser')),
            ],
        ),
    ]
