import http.client
import requests
import hashlib

def connect():
    global connection
    connection = http.client.HTTPConnection("uxhebxje.ddns.net", 1199, timeout=10)
    try:
        connection.request("GET", "/")
    except ConnectionRefusedError:
        return False
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))

def close():
    connection.close

def post(req, val, doPrint=True):
    a = '{"type": "%s", "value": %s}' % (req, val)
    b = str(a)
    if doPrint == True:
        print("sending: " + b)
    response = requests.post(url = "http://uxhebxje.ddns.net:1199", data = b)
    if doPrint == True:
        print("response: " + response.text)
    return response.text

def passman(u, p):
    salt = post("salt", str('"' + u + '"'))
    if salt == "No user found":
        return False
    ap = bytes(p + salt, 'utf-8')
    send = hashlib.sha3_512(ap).hexdigest() + ":" + u
    a = post("login", str('"' + send + '"'))
    return a

def Register(u, p):
    salt = hashlib.sha3_384(bytes(u + p, 'utf-8')).hexdigest()
    b = p + salt
    c = hashlib.sha3_512(bytes(b, 'utf-8')).hexdigest()
    d = salt + ":" + c + ":" + u
    e = post("register", str('"' + d + '"'))
    if e == "Username Already Taken":
        return "uname unav"
    return e

def getUsers(u):
    a = post("GetUsers", str('"' + u + '"'))
    return a

def getMsgHistory(r, u):
    global msgHistory
    msgHistory = post("GetMsgHistory", str('{"s":"' + u + '", "r":"' + r + '"}'), doPrint=False)
    return msgHistory

def send(u, s, r):
    a = '{"msg":"' + s + '", "sender":"' + u + '", "recipient":"' + r + '"}'
    b = post("send", a)
    return b

def messagePoll(u, r):
    a = post("getNewMsgs", '"' + u + ':' + r + '"', doPrint=False)
    return a