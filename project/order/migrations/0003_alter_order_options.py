# Generated by Django 4.1.4 on 2023-02-14 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
