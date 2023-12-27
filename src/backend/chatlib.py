import os
import PySimpleGUI as sg
import sys
sys.path.append("C:/Users/a2kva/Documents/GitHub/SChat/src/frontend")
import frontlib as front

userExists = False

def search_str(file_path, word):
    with open(file_path, "r") as file:
        content = file.read()
        if word in content:
            userExists = True
        else:
            userExists = False

def login(user):
    file_path = "C:/Users/a2kva/Documents/GitHub/SChat/src/backend/userlist.txt"
    if search_str("C:/Users/a2kva/Documents/GitHub/SChat/src/backend/userlist.txt", user) == True:
        return True
    else:
        f = open("C:/Users/a2kva/Documents/GitHub/SChat/src/backend/userlist.txt", "a")
        f.write("\n" + user)
        return False

def new_func():
    return
    
def newchat(recipient):
    os.mkdir("C:/Users/a2kva/Documents/GitHub/SChat/src/backend/chats/" + recipient + "/")

def changeRecipient():
    recipient = input("Who do you want the recipient to be?\n" + open("C:/Users/a2kva/Documents/GitHub/SChat/src/backend/userlist.txt", "r"))

def write(msg, recipient):
    rfile = "C:/Users/a2kva/Documents/GitHub/SChat/src/backend/chats/" + recipient
    f = open(rfile + "/msg.txt", "w")
    f.write(msg)
    f = open(rfile + "/msglist.txt", "a")
    f.write(msg + "\n")
    f = open(rfile + "/msg.txt", "r")
    print(f.read())
    f.close()
    f = open(rfile + "/msglist.txt", "a")
    f.close()