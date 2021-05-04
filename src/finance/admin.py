from django.contrib import admin
from finance.models import FinCategory, FinSource


@admin.register(FinCategory)
class FinCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(FinSource)
class FinSourceAdmin(admin.ModelAdmin):
    pass
