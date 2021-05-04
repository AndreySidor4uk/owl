from django.contrib import admin
from finance.models import FinCategory


@admin.register(FinCategory)
class FinCategoryAdmin(admin.ModelAdmin):
    pass
