from atexit import register
from django.contrib import admin
from accounts.models import UserBankAccount, UserAddress

# Register your models here.


@admin.register(UserBankAccount)
class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_no', 'user']


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'street_address']
