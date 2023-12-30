import os
import PySimpleGUI as sg

dirname = os.path.dirname(__file__)
userlist = os.path.join(dirname, "userlist.txt")
chatsdir = os.path.join(dirname, "chats/")

userExists = False

def search_str(file_path, word):
    with open(file_path, "r") as file:
        content = file.read()
        if word in content:
            userExists = True
        else:
            userExists = False

def login(user):
    file_path = userlist
    if search_str(userlist, user) == True:
        return True
    else:
        f = open(userlist, "a")
        f.write("\n" + user)
        return False
    
def newchat(recipient):
    os.mkdir(chatsdir + recipient + "/")

def changeRecipient():
    recipient = input("Who do you want the recipient to be?\n" + open(userlist, "r"))

def write(msg, recipient):
    rfile = chatsdir + recipient
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
    with open(userlist, "r") as file:
        users = file.read()
        userList = ("a")
        if user in users:
            i += 1
        else:
            return "potata"