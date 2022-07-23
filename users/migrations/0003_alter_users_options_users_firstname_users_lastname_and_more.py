# Generated by Django 4.0.6 on 2022-07-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_user_phone_users_is_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['secondName'], 'verbose_name': 'Пользователь', 'verbose_name_plural': ' Пользователи'},
        ),
        migrations.AddField(
            model_name='users',
            name='firstName',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='users',
            name='lastName',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='users',
            name='secondName',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия'),
        ),
    ]
