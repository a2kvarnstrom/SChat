import http.client

def connect():
    connection = http.client.HTTPConnection("192.168.1.213")
    connection.request("GET", "/")
    response = connection.getresponse()
    print("Status: {} \nReason: {}".format(response.status, response.reason))
    
    connection.close()