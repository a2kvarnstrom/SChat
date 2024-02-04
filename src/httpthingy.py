import http.client
import requests
import hashlib

def connect():
    global connection
    connection = http.client.HTTPConnection("uxhebxje.ddns.net", 1199, timeout=10)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))

def close():
    connection.close

def post(req, val):
    a = '{"type": "' + req + '", "value": "' + val + '"}'
    b = str(a)
    print("sending: " + b)
    response = requests.post(url = "http://uxhebxje.ddns.net:1199", data = b)
    print("response: " + response.text)
    return response.text

def passman(u, p):
    salt = post("salt", u)
    if salt == "No user found":
        return False
    ap = bytes(p + salt, 'utf-8')
    send = hashlib.sha3_512(ap).hexdigest() + ":" + u
    a = post("login", send)
    return a

def Register(u, p):
    salt = hashlib.sha3_384(bytes(u + p, 'utf-8')).hexdigest()
    b = p + salt
    c = hashlib.sha3_512(bytes(b, 'utf-8')).hexdigest()
    d = salt + ":" + c + ":" + u
    e = post("register", d)
    if e == "Username Already Taken":
        return "uname unav"
    return e

def getUsers(u):
    a = post("GetUsers", u)
    return a

def recip(u):
    a = print("\nPlaceholder Code\n")
    return a

def send(u, s, r):
    print("sending: " + '{"type":"send", "value":{"msg":"' + s + '", "sender":"' + u + '", "recipient":"' + r + '"}}')
    a = requests.post(url = "http://uxhebxje.ddns.net:1199", data = '{"type":"send", "value":{"msg":"' + s + '", "sender":"' + u + '", "recipient":"' + r + '"}}').text
    print("response: " + a)
    return a