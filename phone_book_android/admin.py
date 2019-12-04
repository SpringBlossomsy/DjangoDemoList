from django.contrib import admin
from phone_book_android.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    
