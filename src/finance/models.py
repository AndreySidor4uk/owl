from django.db import models
from django.contrib.auth.models import User
from app.models import TimeStampedModel


class FinCategory(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='fin_categories',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Заголовок'
    )

    class Meta:
        unique_together = [
            ['user', 'title']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class FinSource(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='fin_sources',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name='Заголовок'
    )
    category = models.ForeignKey(
        FinCategory,
        on_delete=models.SET_NULL,
        related_name='sources',
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        unique_together = [
            ['user', 'title']
        ]
        verbose_name = 'Источник доходов/расходов'
        verbose_name_plural = 'Источники доходов/расходов'


class FinAccount(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='fin_accounts',
        verbose_name='Пользователь'
    )
    account_number = models.CharField(
        max_length=100,
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
        unique_together = [
            ['user', 'account_number']
        ]
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class FinOperation(TimeStampedModel):
    date = models.DateTimeField(
        verbose_name='Дата операции'
    )
    account = models.ForeignKey(
        FinAccount,
        on_delete=models.CASCADE,
        related_name='operations',
        verbose_name='Счет'
    )
    source = models.ForeignKey(
        FinSource,
        on_delete=models.SET_NULL,
        null=True,
        related_name='operations',
        verbose_name='Источник'
    )
    operation_sum = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Сумма операции'
    )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
