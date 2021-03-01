# Importing libraries
from django.db import models
from datetime import datetime
# Defining of the Customer model to store customers
class Customer(models.Model):
    name = models.CharField(max_length=100) # Customer Name field

    def __str__(self):
        return self.name
# Defining of the Account model to store accounts
class Account(models.Model):
    amount = models.IntegerField(default=100) # Account amount field
    customerID = models.ForeignKey(Customer,on_delete=models.CASCADE) # Customer id field

    def __str__(self):
        return self.customerID.name + " account"
# Defining of the Transaction History model to store transaction histories
class TransactionHistory(models.Model):
    timestamp = models.DateTimeField(default=datetime.now, blank=False) # The field of the time the transaction was performed
    senderAccountID = models.ForeignKey(Account,related_name='senderAccount',on_delete=models.CASCADE) # The account of the sender
    receiverAccountID = models.ForeignKey(Account,related_name='receiverAccount',on_delete=models.CASCADE) # The account of the receiver
    amount = models.IntegerField() # Amount of transaction
    transactionType = models.CharField(max_length=100,default="Undefined") # Type of the transaction

    def __str__(self):
        return "Transaction History"