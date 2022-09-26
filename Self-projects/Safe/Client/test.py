import requests

endpoint = "http://127.0.0.1:8000/api/"
# log in and obtain token - jwt
jwt_login = endpoint + "token/"

response = requests.post(
    jwt_login, json={"username": "tai", "password": "12345"})
print(response.json())
access = response.json()['access']
refresh = response.json()['refresh']

account_endpoints = endpoint + "accounts/"
# accounts = requests.get(account_endpoints, headers={
#                         "Authorization": f"Bearer {access}"})
# print(accounts.json())

# account_endpoints = endpoint + "accounts/"
# new = {'name': 'Maybank', 'balance': 2000.0}
# accounts = requests.post(account_endpoints, headers={
#                          "Authorization": f"Bearer {access}"}, json=new)
# print(accounts.json())

# account_endpoints = endpoint + "accounts/"
# accounts = requests.delete(account_endpoints, headers={
#                            "Authorization": f"Bearer {access}"})
# print(accounts)

# account_endpoints = endpoint + "accounts/6/transactions/"
# new = {'name': 'Maybank', 'balance': 2000.0}
# accounts = requests.get(account_endpoints, headers={
#     "Authorization": f"Bearer {access}"})
# print(accounts.json())

# account_endpoints = endpoint + "accounts/6/transactions/"
# new = {'name': 'Maybank', 'balance': 2000.0}
# accounts = requests.post(account_endpoints, headers={
#     "Authorization": f"Bearer {access}"}, json=new)
# print(accounts.json())

# transactions = endpoint + "transactions"
# response = requests.get(transactions, headers={
#                         "Authorization": f"Bearer {access}"}, params={"tags": 1})
# print(response.json())
