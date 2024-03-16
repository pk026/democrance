# Democrance
Problem stmt (what I understood ;) ):
An agent from a company would 
    1. create a customer
    2. create a quote for the customer
    3. Get the quote reviewed by the customer and mark it accepted
    4. Get the quote paid, and mark the payment
    5. Get detail of the policy
    6. List of policies for a customer
    7. Get history of single policy


# project design and explanation


# stacks used
python, django, djangorestframework, db.sqlite3 (I have kept it to reduce the setup time for you else I would have used postgresql)


# project setup
1. git clone https://github.com/pk026/democrance
2. create a virtualenv using: python3 -m venv venv
3. activate environment using: source venv/bin/activate
4. install requirements using: pip install -r requirements.txt
5. make database setting proper: create a database with name:ola, user:pramod, password: postgres
6. create database schema using: python manage.py migrate
7. create a superuser: python manage.py createsuperuser
8. run: python manage.py runserver


# testbench
