import os
import PySimpleGUI as sg

userExists = False

def search_str(file_path, word):
    with open(file_path, "r") as file:
        content = file.read()
        if word in content:
            userExists = True
        else:
            userExists = False

def login(user):
    file_path = "C:/Users/a2kva/Documents/GitHub/SChat/src/userlist.txt"
    if search_str("C:/Users/a2kva/Documents/GitHub/SChat/src/userlist.txt", user) == True:
        return True
    else:
        f = open("C:/Users/a2kva/Documents/GitHub/SChat/src/userlist.txt", "a")
        f.write("\n" + user)
        return False

def new_func():
    return
    
def newchat(recipient):
    os.mkdir("C:/Users/a2kva/Documents/GitHub/SChat/src/chats/" + recipient + "/")

def changeRecipient():
    recipient = input("Who do you want the recipient to be?\n" + open("C:/Users/a2kva/Documents/GitHub/SChat/src/userlist.txt", "r"))

def write(msg, recipient):
    rfile = "C:/Users/a2kva/Documents/GitHub/SChat/src/chats/" + recipient
    f = open(rfile + "/msg.txt", "w")
    f.write(msg)
    f = open(rfile + "/msglist.txt", "a")
    f.write(msg + "\n")
    f = open(rfile + "/msg.txt", "r")
    print(f.read())
    f.close()
    f = open(rfile + "/msglist.txt", "a")
    f.close()

def fetchUserList():
    i = 0
    with open("C:/Users/a2kva/Documents/GitHub/SChat/src/userlist.txt", "r") as file:
        users = file.read()
        userList = ("a")
        if user in users:
            i += 1
        else:
            return "potata"