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
        post("login", i)

def close():
    connection.close

def post(req, val):
    a = {'type': req, 'value': val}
    print(a)
    response = requests.post(url = "http://uxhebxje.ddns.net:1199", data = a)
    print("response: " + response.text)
    return response.text

def getSalt(user):
    s = post("salt", user)
    return s

def passman(u, p):
    salt = getSalt(u)
    sp = p + salt
    ap = bytes(sp, 'utf-8')
    print("salt: " + salt)
    print("pass: " + p)
    hashpass = hashlib.sha3_512(ap)
    passuser = hashpass.hexdigest() + ":" + u
    print(passuser)
    postLogin(passuser)

'''
import aiohttp
import asyncio

async def post_request():
    url = "http://uxhebxje.ddns.net:1199"
    data = {"key": "value"}

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=data)
        print(await response.json())

asyncio.run(post_request())
''' 