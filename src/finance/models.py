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


class FinSource(TimeStampedModel):
    title = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name='Заголовок'
    )
    category = models.ForeignKey(
        FinCategory,
        on_delete=models.SET_NULL,
        related_name='sources',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Источник доходов/расходов'
        verbose_name_plural = 'Источники доходов/расходов'


class FinAccount(TimeStampedModel):
    account_number = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='Номер/идентификатор счета'
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    balane = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Баланс счета'
    )

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
