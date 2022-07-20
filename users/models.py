from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import User
import uuid


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя на сайте')
    firstName = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя')
    secondName = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия')
    lastName = models.CharField(max_length=200, blank=True, null=True, verbose_name='Отчество')
    user_data_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    user_location = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна')
    user_country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Гражданство')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$") # для валидации
    user_first_phone = PhoneNumberField(unique=True, blank=True, null=True,verbose_name='Мобильный номер')
    user_second_phone = PhoneNumberField(unique=True, blank=True, null=True, verbose_name='Рабочий номер')
    user_email = models.EmailField(max_length=50, blank=True, null=True, verbose_name='Email')
    education = models.CharField(max_length=200, verbose_name="Высшее учебное заведение")
    user_education = models.CharField(max_length=200, blank=True, null=True, verbose_name='Специальность')
    year_ending = models.DateField(blank=True, null=True, verbose_name='Дата окончания учебы')
    is_created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = ' Пользователи'
        ordering = ['secondName']
