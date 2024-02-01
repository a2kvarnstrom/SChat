import http.client
import requests
import hashlib

def connect():
    global connection
    connection = http.client.HTTPConnection("uxhebxje.ddns.net", 1199, timeout=10)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))

def postLogin(i):
    a = post("login", i)
    return a

def close():
    connection.close

def post(req, val):
    a = '{"type": "' + req + '", "value": "' + val + '"}'
    b = str(a)
    response = requests.post(url = "http://uxhebxje.ddns.net:1199", data = b)
    print("response: " + response.text)
    return response.text

def getSalt(user):
    s = post("salt", user)
    return s

def passman(u, p):
    salt = getSalt(u)
    sp = p + salt
    ap = bytes(sp, 'utf-8')
    hashpass = hashlib.sha3_512(ap)
    passuser = hashpass.hexdigest() + ":" + u
    a = postLogin(passuser)
    return a

def Register(u, p):
    a = u + p
    salt = hashlib.sha3_384(bytes(a, 'utf-8'))
    b = p + salt.hexdigest()
    c = hashlib.sha3_512(bytes(b, 'utf-8')).hexdigest()
    d = u + ":" + c
    e = post("register", d)
    return e