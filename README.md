# Dopigo RestAPI Challenge
## About
That project creates a REST API in order to make fake financial institution and manage a bank processes like creating customer, account and establish a transaction between the accounts.

## How it works
Accepts HTTP GET,POST,PUT,PATCH,DELETE Request
* get all the customers (GET /api/getCustomerAll)
* get specified customer with his/her customer id (GET /api/getCustomer/{str:customerID})
* post a new customer (POST /api/addCustomer)
* update a specified customer (PUT /api/updateCustomer/{str:customerID})
* delete a specified customer (DELETE /api/deleteCustomer/{str:customerID})
* get all the accounts (GET /api/getAccountAll)
* get specified account with it's account id (GET /api/getAccount/{str:accountID})
* post a new account related with a customer (POST /api/addAccount)
* update a specified account (PATCH /api/updateAccount/{str:accountID})
* delete a specified account (DELETE /api/deleteAccount/{str:accountID})
* post money among the accounts (POST /api/transferAmounts/)
* post Withdraw money from an account (POST /api/retrieveBalance/)
* get all the transaction has been made (GET /api/getTransactionAll)
* get the transaction history for specified account (GET /api/getTransaction/{str:accountID})
* If the project environment empty you can create an environment with random users, accounts and random transactions
* In order to this (GET /api/initEnvironment)
* In order to deleting the current environment (GET /api/deleteAllCustomers)

## Example of use cases
1. To getting all the customers
* http://127.0.0.1:8000/api/getCustomerAll/
2. To getting specified customer with his/her customer id
* http://127.0.0.1:8000/api/getCustomer/8233
3. To creating a new customer
* http://127.0.0.1:8000/api/addCustomer/ (As a POST Request) ({
    "name":"customer_name"
})
4. To updating specified customer
* http://127.0.0.1:8000/api/updateCustomer/8233/ (As a PUT Request) (
{
    "name":"customer_name_update"
}
)
5. To deleting specified customer (As a DELETE Request)
* http://127.0.0.1:8000/api/deleteCustomer/8232
6. To getting all the accounts
* http://127.0.0.1:8000/api/getAccountAll/ (As a GET Request)
7. To getting specified account
* http://127.0.0.1:8000/api/getAccount/24637 (As a GET Request)
8. To creating a new account (As a POST Request)
* http://127.0.0.1:8000/api/addAccount/
({
    "amount":4800,
    "customerID":98
})
9. To updating a specified account (As a PATCH Request)
* http://127.0.0.1:8000/api/updateAccount/24637/
({
    "amount":4800
})
10. To deleting a specified account (As a DELETE Request)
* http://127.0.0.1:8000/api/deleteAccount/24637
11. To posting money among the accounts (As a POST Request)
* http://127.0.0.1:8000/api/transferAmounts/
({

    "fromAccount":18620, # Account ID
    "toAccount":18621, # Account ID
    "amount":700 # Value of the sending money
}
)
12. To withdrawing a money from an account (As a POST Request)
* http://127.0.0.1:8000/api/retrieveBalance/
({
    "accountID":21620, 
    "amount": 1500
})
13. To getting all the transactions has been made (As a GET Request)
* http://127.0.0.1:8000/api/getTransactionAll/
14. To getting transaction history for a specified account (As a GET Request)
* http://127.0.0.1:8000/api/getTransaction/26991
15. To creating an environment to using the rest api (As a GET Request)
* http://127.0.0.1:8000/api/initEnvironment/
16. To deleting an existing environment (As a GET Request)
* http://127.0.0.1:8000/api/deleteAllCustomers/

# Requirements
* asgiref==3.3.1
* attrs==20.3.0
* Django==3.1.7
* djangorestframework==3.12.2
* gunicorn==20.0.4
* iniconfig==1.1.1
* packaging==20.9
* pluggy==0.13.1
* py==1.10.0
* pyparsing==2.4.7
* pytest==6.2.2
* pytest-django==4.1.0
* pytz==2021.1
* sqlparse==0.4.1
* toml==0.10.2
## Technologies
In this project, For the backend language Python was used and Django was used as a framework.
For the database, Sqlite was used.
## Installation and Run
To run the code:

###### On terminal:
 ```bash
cd BankAPI
pip install -r requirements.txt
python manage.py runserver
```

Alternately, to quickly try out this repo in the cloud, [You can access to project on heroku!](https://dopigorestchallenge.herokuapp.com/getCustomerAll)
###### On Docker compose: 
Type the following command on your terminal
```bash
docker-compose up
```
###### View
```bash
http://0.0.0.0:5000/api/getCustomerAll/
```
###### Stop
```bash
docker-compose stop
```
###### To running with Docker file on your host: 
Type the following command on your terminal
```bash
docker build --tag <Enter a tag name> .
```
Then,
```bash
docker run --rm -i -t <Your tag name> (This path run the code on your)
```
If you want to map the port and acces on your local machine:
```bash
docker run -rm -i -t -p 8080:5000 <Your tag name>(This path run the code on your)
```
# Test
In order to test the project, type the following command on your terminal
```bash
npm test

```
