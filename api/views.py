# Importing the libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from .models import Customer
from .models import Account
from .models import TransactionHistory
from .serializers import Customer as serializeCustomer
from .serializers import Account as serializeAccount
from .serializers import TransactionHistory as serializeTransaction
from django.views.decorators.csrf import csrf_exempt
from time import gmtime, strftime
import json
import random


# That function handles with /getCustomerAll request
# Getting all the customers from database and display them as a json
def getCustomerAll(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = serializeCustomer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)
# That function handles with /getCustomer/<str:customerID> request
# Getting the specific customer from database and display it as a json
def getCustomer(request,customerID):
   if request.method == 'GET':
           customer = Customer.objects.get(id=customerID)
           serializer = serializeCustomer(customer, many=False)
           return JsonResponse(serializer.data, safe=False)
   else:
       return HttpResponse(status=404)
# That function handles with /addCustomer request
# Adding the new customer
@csrf_exempt
def addCustomer(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializeCustomer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return HttpResponse(status=400)
# That function handles with /updateCustomer/<str:customerID> request
# Updating the requested customer
@csrf_exempt
def updateCustomer(request,customerID):
    if request.method == 'PUT':
        if customerID is not None:
            customer = Customer.objects.get(id=customerID)
            data = JSONParser().parse(request)
            serializer = serializeCustomer(customer, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, safe=400)
    else:
        return HttpResponse(status=400)
# That function handles with /deleteCustomer/<str:customerID> request
# Deleting the requested customer
@csrf_exempt
def deleteCustomer(request,customerID):
    if request.method == 'DELETE':
        if customerID is not None:
            customer = Customer.objects.get(id=customerID)
            customer.delete()
            return JsonResponse("Customer has been deleted.", safe=False)
    else:
        return HttpResponse(status=400)
# That function handles with /getAccountAll request
# Getting all the accounts from database and display them as a json
def getAccountAll(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = serializeAccount(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=404)
# That function handles with /getAccount/<int:accountID> request
# Getting the specific account from database and display it as a json
def getAccount(request,accountID):
    if request.method == 'GET':
        account = Account.objects.get(id=accountID)
        serializer = serializeAccount(account, many=False)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=404)
# That function handles with /addAccount request
# Adding the new account
@csrf_exempt
def addAccount(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializeAccount(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse("Customer Does Not Exist.", safe=False)
# That function handles with /updateAccount/<str:accountID>' request
# Updating the requested account with specified field
@csrf_exempt
def updateAccount(request,accountID):
    if request.method == 'PATCH':
        if accountID is not None:
            account = Account.objects.get(id=accountID)
            data = JSONParser().parse(request)
            serializer = serializeAccount(account, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, safe=400)
    else:
        return HttpResponse(status=400)
# That function handles with /deleteAccount/<str:accountID>' request
# Deleting the specified account from database
@csrf_exempt
def deleteAccount(request,accountID):
    if request.method == 'DELETE':
        if accountID is not None:
            account = Account.objects.get(id=accountID)
            account.delete()
            return JsonResponse("Account has been deleted.", safe=False)
    else:
        return HttpResponse(status=400)
# That function creates a TransactionHistory instance when a transaction has been made.
# When a user withdrawn some money from his/her account or send money to another account
def TransactionRegisters(senderID,receiverID,amount,transactionType):
    senderAccount = Account.objects.get(id=senderID)
    receiverAccount = Account.objects.get(id=receiverID)
    transaction = TransactionHistory(senderAccountID=senderAccount,receiverAccountID=receiverAccount,amount=amount,transactionType=transactionType)
    transaction.save()
    serializer = serializeTransaction(data=transaction)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Account has been deleted.", safe=False)
# That function is the logic of transferring money among the accounts.
# It takes customer's account's ids and the value of the amount.
# If the sender user's account will not be lower than zero after the transaction, process made
# Otherwise display the error message
def amountTransfer(fromAccountID,toAccountID,amount):
    fromAccount = Account.objects.get(id=fromAccountID)
    serializerFromAccount = serializeAccount(fromAccount, many=False)
    toAccount = Account.objects.get(id=toAccountID)
    serializerToAccount = serializeAccount(toAccount, many=False)
    fromAccountJson = serializerFromAccount.data
    toAccountJson = serializerToAccount.data
    if(fromAccountJson['amount']-amount < 0):
        resultJson={
            "Message":"Sender Account's Balance Is Not Enough",
            "Sender": {
                "SenderID":fromAccountID,
                "Sendin Amount":amount
            },
            "Receiver": {
                "ReceiverID":toAccountID
            }
        }
        return resultJson
    else:
        fromAccountJson['amount'] -= amount
        toAccountJson['amount'] += amount
        AfterOperationSerializerFromAccount = serializeAccount(fromAccount, data=fromAccountJson)
        AfterOperationSerializerToAccount = serializeAccount(toAccount, data=toAccountJson)
        if AfterOperationSerializerFromAccount.is_valid() and AfterOperationSerializerToAccount.is_valid():
            AfterOperationSerializerFromAccount.save()
            AfterOperationSerializerToAccount.save()
            TransactionRegisters(fromAccountID,toAccountID,amount,"Transfer amounts")
            resultJson = {
                "Message": "Transactions is successfully completed.",
                "Sender": {
                    "SenderID": fromAccountID,
                    "Sending Amount": amount
                },
                "Receiver": {
                    "ReceiverID": toAccountID
                }
            }
            return resultJson
# That function handles with /transferAmounts' request
# Transferring money among the specified accounts
@csrf_exempt
def transferAmounts(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        resultJson=amountTransfer(data['fromAccount'], data['toAccount'], data['amount'])
        return JsonResponse(resultJson,safe=False)
    else:
        return JsonResponse("Transaction Error.",safe=False)
# That function is the logic of Withdrawing money from specified account.
# Withdraw the desired amount from the specified account
# It takes account id and the value of the amount.
# If the customer's account will not be lower than zero after the transaction, process made
# Otherwise display the error message
def retrieveAmount(accountID,amount):
    currentAccount = Account.objects.get(id=accountID)
    serializerCurrentAccount = serializeAccount(currentAccount, many=False)
    currentAccountJson = serializerCurrentAccount.data
    if(currentAccountJson['amount'] - amount < 0):
        resultJson={
            "Message: ":"The account balance is insufficient for the transaction.",
            "accountID": currentAccountJson['id'],
            "amount":currentAccountJson['amount'],
            "customerID":currentAccountJson['customerID']
        }
        return JsonResponse(resultJson, safe=False)
    else:
        currentAccountJson['amount'] -= amount
        AfterOperationSerializerCurrentAccount = serializeAccount(currentAccount, data=currentAccountJson)
        if AfterOperationSerializerCurrentAccount.is_valid():
            AfterOperationSerializerCurrentAccount.save()
            TransactionRegisters(accountID,accountID,amount,"Retrieve balances")
            resultJson = {
                "Message: ": "Transaction completed.",
                "accountID": currentAccountJson['id'],
                "amount": currentAccountJson['amount'],
                "customerID": currentAccountJson['customerID']
            }
            return JsonResponse(resultJson, safe=False)
# That function handles with /retrieveBalance' request
# Withdraw the desired amount from the specified account
@csrf_exempt
def retrieveBalance(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = retrieveAmount(data['accountID'],data['amount'])
        return result
    else:
        return JsonResponse("Transaction Error.",safe=False)
# That function handles with /getTransactionAll' request
# Getting all the transaction histories from the database
def getTransactionAll(request):
    if request.method == 'GET':
        transaction = TransactionHistory.objects.all()
        serializer = serializeTransaction(transaction, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)
# That function handles with /getTransaction/<str:accountID>' request
# Getting specified account's transaction history
def getTransaction(request,accountID):
    if request.method == 'GET':
        transactionSender = TransactionHistory.objects.filter(senderAccountID=accountID)
        transactionReceiver = TransactionHistory.objects.filter(receiverAccountID=accountID)
        serializerSender = serializeTransaction(transactionSender, many=True)
        serializerReceiver = serializeTransaction(transactionReceiver, many=True)
        register = []
        register.append(serializerSender.data)
        register.append(serializerReceiver.data)
        registerString = json.dumps(register.pop(),indent=4)
        registerJson = json.loads(registerString)
        return JsonResponse(registerJson,safe=False)
    else:
        return HttpResponse(status=400)
# That function creates 1000 customer's
# In order to initializing the starting environment
def createCustomers():
    for i in range(1, 1001):
        c = Customer(name="User" + str(i))
        c.save()
# That function creates 3000 customer's
# In order to initializing the starting environment
def createAccounts():
    customerList = Customer.objects.all()
    for i in range(1,3001):
        amount = random.randint(5000,90000)
        newcustomerID = random.choice(customerList)
        account = Account(amount=amount,customerID=newcustomerID)
        account.save()
# That function makes 5000 random transactions among the random accounts
# In order to initializing the starting environment
def createRandomTransaction():
    #Getting account list
    accountIdList = Account.objects.values_list('id', flat=True)
    print("Account list: ",accountIdList)
    # Selection Transaction Type 1- Retrieve Balance 2- Transfer Amount
    for i in range(1,5001):
        transActionType = random.randint(1,2)
        if (transActionType==1):
            amount = random.randint(1000, 2000)
            newAccountID = random.choice(accountIdList)
            retrieveAmount(newAccountID,amount)
        elif (transActionType==2):
            amount = random.randint(1000, 2000)
            newAccountIDFrom = random.choice(accountIdList)
            newAccountIDTo = random.choice(accountIdList)
            amountTransfer(newAccountIDFrom,newAccountIDTo,amount)
        else:
            return JsonResponse("Error occured on process.",safe=False)
# That function deletes all the instances from database
# Resets the environment
def deleteAllCustomers(request):
    if request.method == 'GET':
        Customer.objects.all().delete()
        return JsonResponse("All customers has been deleted.",safe=False)
# That function starts the environment
# In order to using the restAPI's functionalities
def initEnvironment(request):
    if request.method == 'GET':
        #Creating 1000 customers
        createCustomers()
        #Creating 3000 accounts
        createAccounts()
        #Creating 5000 transactions
        createRandomTransaction()
        return JsonResponse({
            "Message":"The Environment Successfully Created.",
            "Number Of Created Customer":1000,
            "Number Of Created Accounts":3000,
            "Number Of Created Transaction":5000
        })

