# Generated by Django 3.2 on 2023-04-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_portfolio_technologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
