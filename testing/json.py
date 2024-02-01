import json 

database = "C:/Users/a2kva/Documents/GitHub/SChat/testing/file.json"
data = json.loads(open(database).read())

id_number = data[1]["id_number"]
print(id_number)
print(list(map(lambda x:x if x["id_number"]=="cz1093" else print("kys"), data)))