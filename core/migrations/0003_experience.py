# Generated by Django 3.2 on 2023-04-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(default='current', max_length=7)),
                ('institution_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]