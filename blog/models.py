from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Article(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=200,
        null=True,
        db_index=True,
        unique=True,
    )
    discripton = models.TextField(
        'Описание',
        null=True,
        blank=True,
        default='Нет записей'
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    CATEGORY = (
        (1, "Спорт"),
        (2, "Политика"),
        (3, "Культура"),
        (4, "Криптавалюта"),
        (5, "Фильмы"),
        (6, "Сериалы"),
    )
    category = models.CharField(
        'Категории',
        choices=CATEGORY,
        blank=True,
        max_length=200
    )
    image = models.ImageField(
        'Изображение',
        upload_to='images/'
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
