# Generated by Django 5.0 on 2025-01-22 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
