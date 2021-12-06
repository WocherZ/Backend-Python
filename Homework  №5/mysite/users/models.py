from django.db import models


class User(models.Model):
    first_name = models.CharField(
        max_length=32,
        verbose_name='Имя',
        null=False,
    )
    last_name = models.CharField(
        max_length=32,
        verbose_name='Фамилия',
        null=False
    )
    user_email = models.EmailField(
        verbose_name='Почта',
        null=True,
    )
    password = models.CharField(
        max_length=32,
        verbose_name='Пароль',
        null=False
    )

    def __str__(self):
        return f"{self.last_name}  {self.first_name}"

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ['last_name']

