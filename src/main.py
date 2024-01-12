import http.client

connection = http.client.HTTPConnection('www.python.org')
connection.request('GET', '/')
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()
