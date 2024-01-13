import http.client

def connect():
    c =  http.client.HTTPConnection("192.168.1.213", 1199, timeout=10)
    c.request("GET", "/")
    response = c.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))
    connect.close = c.close()