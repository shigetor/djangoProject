# Generated by Django 4.0.6 on 2022-07-20 10:54

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_phone',
        ),
        migrations.AddField(
            model_name='users',
            name='is_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_first_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Мобильный номер'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_second_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Рабочий номер'),
        ),
        migrations.AlterField(
            model_name='users',
            name='education',
            field=models.CharField(max_length=200, verbose_name='Высшее учебное заведение'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_data_birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_education',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя на сайте'),
        ),
        migrations.AlterField(
            model_name='users',
            name='year_ending',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания учебы'),
        ),
    ]
