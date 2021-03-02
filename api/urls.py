# Importing path library
# Importing all the views that RestAPI uses from views class
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

# Storing url's in order to use their functionalities which were written in views class
# The URL patterns list routes URLs to views.
urlpatterns = [
    path('getCustomerAll/',getCustomerAll, name="getCustomerAll"),
    path('getCustomer/<str:customerID>',getCustomer, name="getCustomer"),
    path('addCustomer/', addCustomer, name="addCustomer"),
    path('updateCustomer/<str:customerID>', updateCustomer, name="updateCustomer"),
    path('deleteCustomer/<str:customerID>', deleteCustomer, name="deleteCustomer"),
    path('getAccountAll/',getAccountAll, name="getAccountAll"),
    path('getAccount/<str:accountID>', getAccount,name="getAccount"),
    path('addAccount/', addAccount, name="addAccount"),
    path('updateAccount/<str:accountID>',updateAccount, name="updateAccount"),
    path('deleteAccount/<str:accountID>',deleteAccount, name="deleteAccount"),
    path('transferAmounts/',transferAmounts, name="transferAmounts"),
    path('retrieveBalance/', retrieveBalance, name="retrieveBalance"),
    path('getTransactionAll/', getTransactionAll, name="getTransactionAll"),
    path('getTransaction/<str:accountID>',getTransaction,name="getTransaction"),
    path('initEnvironment/',initEnvironment),
    path('deleteAllCustomers/',deleteAllCustomers)
]
