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
    a = {'type': req,
            'value': val}
    
    response = requests.post(url = "http://192.168.0.123:1199", data = a)
    print(response.text)
    return response.text

def getSalt(user):
    s = post("salt", user)
    return s