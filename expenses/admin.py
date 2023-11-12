from django.contrib import admin
from .models import Expense, AccountInfo, Category
# Register your models here.

admin.site.register(Expense)
admin.site.register(AccountInfo)
admin.site.register(Category)