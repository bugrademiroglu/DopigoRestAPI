from django.contrib import admin
from . models import Customer
from . models import Account
from .models import TransactionHistory

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(TransactionHistory)