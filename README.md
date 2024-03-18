
# Democrance

## Problem Statements:
1. Customer does signup.
2. Creates a quote.
3. Reviewed the quote and marks it accepted.
4. Does the payment/start the policy and backend gets the bill paid by payment link or something.
5. Get detail of the policy.
6. List of policies.
7. Get history of a single policy.

## Project Design and Explanation

1. Part 1: Create customer

    There could be two ways to use this endpoint:
    a. Customer post his information along with name, dob, email/phone, password (basically does the signup)
    b. A staff from insurance company can post above information and customer gets the link to set password

    The post body for customer probably is not enough, we should post with one unique identifier
    e.g. Phone or email
    We can create a User (I am talking about django user here), and put a one-to-one mapping with Customer table.

    ```bash
    {
        "first_name": "Ben",
        "last_name": "Stokes",
        "dob": "25-06-1991"
    }

2. Part 2: Create quote
    Quote information could be posted by a staff user, along with customer
    ```bash
     {
        "type": "personal-accident",
        "premium": 200,
        "cover": 200000
        "state": "new",
        "customer": 1,

    }

Also the customer himself could login, and post the quote attributes and on backend we can fetch the customer from logged in user and can fill in before creating the quote

3. Part 3: Implement search for customers/policies. Find customers by name, dob or policy type.

    1. On django admin: added filter on policy: filter by name, dob and policy type
    2. On django admin: added filter on customer: filter by name, dob

4. Discuss how you would implement authentication for users/customers, and would these be the same or different?

    Since we are already using Django REST Framework we can utilise `rest_framework authtoken` for authentication, So we can use token based authentiocation, for this we will expose one login API which validates the user credentials and returns a token which could be used in subsequent requests,

    User does not have to be customer necesarily, user could be staff user as well, if user is customer user will have a one-to-one mapping with customer.


## Stacks Used
- Python
- Django
- Django REST Framework
- SQLite3 (Note: SQLite3 is used to reduce the setup time. PostgreSQL would be preferred for production environments.)

## Project Setup

To get the project up and running on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/pk026/democrance
2. Create a virtualenv using:
     ```bash
     python3 -m venv venv
3. Activate environment using:
   ```bash
     source venv/bin/activate
4. Install requirements using:
     ```bash
    pip install -r requirements.txt
5. Create database schema using:
    ```bash
        python manage.py migrate
6. Create a superuser:
    ```bash
    python manage.py createsuperuser --username admin --email admin@example.com
7. run development server:
    ```bash
    python manage.py runserver

## Testing
