from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=32,
        verbose_name='Название категории',
        unique=True
        )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Список категорий'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(
        verbose_name='Название продукта',
        max_length=32,
        null=False,
        blank=False
        )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория продукта',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
        )

    product_image = models.ImageField(
        verbose_name='Картинка продукта',
        null=True,
        blank=True,
        )

    description = models.TextField(
        verbose_name='Описание продукта',
        null=True,
        blank=True,
        )

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Список продуктов'
        ordering = ['product_name']

