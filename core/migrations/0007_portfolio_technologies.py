# Generated by Django 3.2 on 2023-04-30 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_portfolio_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='technologies',
            field=models.JSONField(null=True),
        ),
    ]
