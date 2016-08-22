import json
import requests

USER = "tester"
URL = "http://localhost:5000/"


def get_user_balance():
    user = USER
    response = requests.get("{}transaction/".format(URL), data={'user': user})
    response_json = json.loads(response.text)

    return response_json['data']['balance']


def save_loan(friend, amount, type):
    user = USER

    if type == "lend":
        creditor = user
        debtor = friend
    else:
        creditor = friend
        debtor = user

    data = {
        "creditor": creditor,
        "debtor": debtor,
        "value": amount,
    }

    r = requests.post("{}transaction/".format(URL), data=data)

    print(r.text)
    print(friend)
    print(amount)
    print(type)
