# Generated by Django 4.1.5 on 2023-03-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyticket', '0002_alter_payment_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
    ]
