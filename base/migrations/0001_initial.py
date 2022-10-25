# Generated by Django 4.0.5 on 2022-10-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Primeiro nome')),
                ('second_name', models.CharField(max_length=30, verbose_name='Segundo nome')),
                ('tell', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
