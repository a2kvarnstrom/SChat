import http.client
import requests

def connect():
    global connection
    connection = http.client.HTTPConnection("192.168.0.123", 1199, timeout=10)
    connection.request("POST", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))


def close():
    connection.close

def post(req, val):
    print(req + "\n" + val)

    data = {'type': req,
            'value': val}
    
    requests.post(url="192.168.0.123", data=data)

def getSalt(user):
    salt = post(salt, user)
    return salt