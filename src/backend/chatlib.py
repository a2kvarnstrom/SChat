import os

userExists = False

def search_str(file_path, word):
    with open(file_path, "r") as file:
        content = file.read()
        if word in content:
            userExists = True
        else:
            userExists = False

def login():
    user = input("Enter your username:\n")
    if search_str("./src/userlist.txt", user) == True:
        return
    else:
        f = open("./src/userlist.txt", "a")
        f.write(user)
    
def newchat(recipient):
    os.mkdir("./src/chats/" + recipient + "/")

def changeRecipient():
    recipient = input("Who do you want the recipient to be?\n" + open("./src/userlist.txt", "r"))

def write(msg, recipient):
    rfile = "./src/chats/" + recipient
    f = open(rfile + "/msg.txt", "w")
    f.write(msg)
    f = open(rfile + "/msglist.txt", "a")
    f.write(msg + "\n")
    f = open(rfile + "/msg.txt", "r")
    print(f.read())
    f.close()
    f = open(rfile + "/msglist.txt", "a")
    f.close()