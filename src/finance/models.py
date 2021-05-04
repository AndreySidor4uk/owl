from django.db import models
from app.models import TimeStampedModel


class FinCategory(TimeStampedModel):
    title = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name='Заголовок'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
