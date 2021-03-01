"""
Serializer stands for converting complex data to python datatypes.
In order to see responses as a json.

"""

# Importing the libraries
from rest_framework import serializers
from .models import Customer
from .models import Account
from .models import TransactionHistory
# Creating Customer class in order to deal with Customer Queryset
class Customer(serializers.ModelSerializer):
    class Meta:
        model = Customer # Defining the serializes model
        fields = ['id','name'] # Setting field name and field instance
# Creating Account class in order to deal with Account Queryset
class Account(serializers.ModelSerializer):
    class Meta:
        model = Account # Defining the serializes model
        fields = ['id','amount','customerID'] # Setting field name and field instance
        extra_kwargs = {'customerID': {'required': False}}
# Creating TransactionHistory class in order to deal with TransactionHistory Queryset
class TransactionHistory(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory # Defining the serializes model
        fields = ['id', 'timestamp', 'senderAccountID','receiverAccountID','amount','transactionType'] # Setting field name and field instance