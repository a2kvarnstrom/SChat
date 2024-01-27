import http.client

def connect():
    c = http.client.HTTPConnection("192.168.0.123", 1199, timeout=10)
    c.request("POST", "/")
    response = c.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))
    connect.close = c.close()

def post(type):
    print(type)