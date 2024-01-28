import http.client
import requests

def connect():
    global connection
    connection = http.client.HTTPConnection("uxhebxje.ddns.net", 1199, timeout=10)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))

def postLogin(i):
        post("login", i)

def close():
    connection.close

def post(req, val):
    a = {'type': req,
            'value': val}
    
    response = requests.post(url = "http://uxhebxje.ddns.net:1199", data = a)
    return response.text

def getSalt(user):
    s = post("salt", user)
    return s