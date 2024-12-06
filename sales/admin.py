from django.contrib import admin
from .models import sale

@admin.register(sale)
class saleAdmin(admin.ModelAdmin):
    list_display = ('data','produto','quantidade','price')
