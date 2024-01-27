import http.client

def connect():
    global connection
    connection = http.client.HTTPConnection("192.168.0.123", 1199, timeout=10)
    connection.request("POST", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))


def close():
    connection.close

def post(type):
    print(type)

def getSalt():
    print("hi")