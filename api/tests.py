# Importing the libraries
from django.urls import reverse
from django.http import request, response, HttpResponse, JsonResponse
from django.test import *
from .models import *
import json
from datetime import datetime
# Initializing the test class
class TestClass(TestCase):
    # Creating a test customer and test account
    def setUp(self):
        Customer.objects.create(name="Test")
        test_User_CustomerID = Customer.objects.get(name="Test")
        Account.objects.create(amount=999999,customerID=test_User_CustomerID)
    # Creating a function in order to the test /getCustomer/<id> route with GET request
    def test_customer_get(self):
        test_User_CustomerID = Customer.objects.get(name="Test")
        customer = Customer.objects.get(id=test_User_CustomerID.id)
        first_customer_url = f"/api/getCustomer/{customer.name}"
        self.assertEqual(first_customer_url,reverse('getCustomer', args=[str(customer.name)]))
    # Creating a function in order to the test /getCustomerAll route with GET method
    def test_customer_getCustomerAll(self):
        c = Client()
        response = c.get(
            '/api/getCustomerAll/',
        )
        self.assertEqual(response.status_code, 200)
    # Creating a function in order to the test /addCustomer route with POST method
    # That test function tests to adding new customer
    def test_adding_new_Customer(self):
            c= Client()
            response = c.post(
                f'/api/addCustomer/',
                {'name': "NewTestUser"},
                content_type='application/json'
            )
            res = response.content.decode("utf-8")
            data = json.loads(res)
            customer = Customer.objects.get(name="NewTestUser")
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data['id'],customer.id)
            self.assertEqual(data['name'], customer.name)
    # Creating a function in order to the test /updateCustomer route with PUT method
    # That test function tests to updating existing customer
    def test_update_customer(self):
            c= Client()
            updateCustomer = Customer.objects.get(name="Test")
            response = c.put(
                f'/api/updateCustomer/{updateCustomer.id}',
                {'name': "UpdatedNewTestUser"},
                content_type='application/json'
            )
            res = response.content.decode("utf-8")
            data = json.loads(res)
            customer = Customer.objects.get(name="UpdatedNewTestUser")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['id'], customer.id)
            self.assertEqual(data['name'], customer.name)
    # Creating a function in order to the test /deleteCustomer/<id>  route with DELETE method
    # That test function tests to deleting existing customer
    def test_delete_customer(self):
            c= Client()
            updateCustomer = Customer.objects.get(name="Test")
            response = c.delete(
                f'/api/deleteCustomer/{updateCustomer.id}'
            )
            res = response.content.decode("utf-8")
            data = json.loads(res)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data,"Customer has been deleted.")
    # Creating a function in order to the test /getAccountAll route with GET method
    # That test function tests to displaying all the account as a json
    def test_account_getAccountAll(self):
        c = Client()
        response = c.get(
            '/api/getAccountAll/',
        )
        self.assertEqual(response.status_code, 200)
    # Creating a function in order to the test /getAccount/<id> route with GET method
    # That test function tests to displaying requested account with it's id as a json
    def test_account_getAccount(self):
        test_Account = Account.objects.get(id=1)
        account_url = f"/api/getAccount/{test_Account.id}"
        self.assertEqual(account_url,reverse('getAccount', args=[str(test_Account.id)]))
    # Creating a function in order to the test /addAccount route with POST method
    # That test function tests to adding new account to a existing customer
    def test_adding_new_Account(self):
        Customer.objects.create(name="Test_Adding_New_Account")
        test_User_CustomerID = Customer.objects.get(name="Test_Adding_New_Account")
        test_customer_id = test_User_CustomerID.id
        c = Client()
        response = c.post(
            '/api/addAccount/',
            {'amount': 9999999999,
             'customerID':test_customer_id
             },
            content_type='application/json'
        )
        res = response.content.decode("utf-8")
        data = json.loads(res)
        account = Account.objects.get(customerID=test_customer_id)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['amount'], account.amount)
        self.assertEqual(data['customerID'], test_customer_id)
    # Creating a function in order to the test /updateAccount/<id> route with PATCH method
    # That test function tests to updating specific field at requested account
    def test_update_Account(self):
        Customer.objects.create(name="updateAccount")
        test_User_CustomerID = Customer.objects.get(name="updateAccount")
        Account.objects.create(amount=1, customerID=test_User_CustomerID)
        test_customer_id = test_User_CustomerID.id
        c = Client()
        response = c.patch(
            f'/api/updateAccount/{test_customer_id}',
            {'amount': 19999999999
             },
            content_type='application/json'
        )
        res = response.content.decode("utf-8")
        data = json.loads(res)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], 2)
        self.assertEqual(data['amount'], 19999999999)
    # Creating a function in order to the test /deleteAccount/<id> route with DELETE method
    # That test function tests to deleting existing account
    def test_delete_account(self):
        Customer.objects.create(name="updateAccount")
        test_User_CustomerID = Customer.objects.get(name="updateAccount")
        Account.objects.create(amount=1, customerID=test_User_CustomerID)
        test_customer_id = test_User_CustomerID.id
        c = Client()
        response = c.delete(
            f'/api/deleteAccount/{test_customer_id}'
        )
        res = response.content.decode("utf-8")
        data = json.loads(res)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, "Account has been deleted.")
    # Creating a function in order to the test /transferAmounts route with POST method
    # That test function tests to transferring money from one account to another
    def test_transferAmount(self):
        Customer.objects.create(name="test_from_user")
        Customer.objects.create(name="test_to_user")
        test_from_user = Customer.objects.get(name="test_from_user")
        test_to_user = Customer.objects.get(name="test_to_user")
        Account.objects.create(amount=20000, customerID=test_from_user)
        Account.objects.create(amount=10000, customerID=test_to_user)
        c = Client()
        response = c.post(
            '/api/transferAmounts/',
            {'fromAccount': test_from_user.id,
             'toAccount':test_to_user.id,
             'amount':5000
             },
            content_type='application/json'
        )
        res = response.content.decode("utf-8")
        data = json.loads(res)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Message'], "Transactions is successfully completed.")
    # Creating a function in order to the test /retrieveBalance route with POST method
    # That test function tests the withdrawal from the account.
    def test_retrieveBalance(self):
        Customer.objects.create(name="test_from_user")
        test_from_user = Customer.objects.get(name="test_from_user")
        Account.objects.create(amount=20000, customerID=test_from_user)
        c = Client()
        response = c.post(
            '/api/retrieveBalance/',
            {'accountID': test_from_user.id,
             'amount':5000
             },
            content_type='application/json'
        )
        res = response.content.decode("utf-8")
        data = json.loads(res)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['Message: '], "Transaction completed.")
    # Creating a function in order to the test /getTransactionAll route with GET method
    # That test function tests to displaying all the transaction which have been made.
    def test_transactionAll(self):
        c = Client()
        response = c.get(
            '/api/getTransactionAll/',
        )
        self.assertEqual(response.status_code, 200)
    # Creating a function in order to the test /getTransaction<id> route with GET method
    # That test function tests to displaying requested account's transactions.
    def test_transaction(self):
        customerFrom = Customer.objects.create(name="test_from_user")
        customerTo = Customer.objects.create(name="test_to_user")
        fromAccount = Account.objects.create(amount=999999,customerID=customerFrom)
        toAccount = Account.objects.create(amount=999999, customerID=customerTo)
        transAction = TransactionHistory.objects.create(senderAccountID=fromAccount,receiverAccountID=toAccount,amount=1234,transactionType="Transfer amounts")
        test_Transaction = TransactionHistory.objects.get(id=1)
        account_url = f"/api/getTransaction/{test_Transaction.id}"
        self.assertEqual(account_url,reverse('getTransaction', args=[str(test_Transaction.id)]))

