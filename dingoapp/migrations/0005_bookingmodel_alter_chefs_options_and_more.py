# Generated by Django 4.2.5 on 2023-09-29 04:50

import dingoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dingoapp', '0004_alter_category_options_alter_chefs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('num_of_g', models.IntegerField(verbose_name='Number of guests')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone number')),
                ('date', models.DateTimeField(validators=[dingoapp.models.past_date_validator], verbose_name='Date')),
                ('time', models.TimeField(validators=[dingoapp.models.past_time_validator], verbose_name='Time')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
            ],
        ),
        migrations.AlterModelOptions(
            name='chefs',
            options={'verbose_name': 'Chef', 'verbose_name_plural': 'Chefs'},
        ),
        migrations.AlterField(
            model_name='chefs',
            name='X_twitter',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='X'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='facebook',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='instagram',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='skype',
            field=models.URLField(blank=True, default='#', null=True, verbose_name='Skype'),
        ),
    ]