# Generated by Django 4.1.1 on 2022-09-24 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_users_options_users_firstname_users_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя на сайте')),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('secondName', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия')),
                ('lastName', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
                ('user_data_birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('user_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('user_country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Гражданство')),
                ('user_first_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Мобильный номер')),
                ('user_second_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Рабочий номер')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('education', models.CharField(max_length=200, verbose_name='Высшее учебное заведение')),
                ('user_education', models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальность')),
                ('year_ending', models.DateField(blank=True, null=True, verbose_name='Дата окончания учебы')),
                ('is_created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': ' Пользователи',
                'ordering': ['is_created'],
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
