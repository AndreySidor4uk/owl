from django.contrib import admin
from finance.models import FinCategory, FinSource, FinAccount


@admin.register(FinCategory)
class FinCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(FinSource)
class FinSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(FinAccount)
class FinAccountAdmin(admin.ModelAdmin):
    pass
