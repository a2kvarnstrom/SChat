import httpthingy as c
import PySimpleGUI as sg 
import bcrypt

def passcrypt(p):
    salt = c.getSalt()
    hashpass = bcrypt.hashpw(p, salt)
   
c.connect()

sg.theme("Black")
layout = [
    [sg.Text("Enter your Username"), sg.InputText()],
    [sg.Text("Enter your Password"), sg.InputText()],
    [sg.Button("Enter"), sg.Button("Cancel")]
]
curwin = sg.Window("Login", layout)
event, values = curwin.read()
while True:
    if event == "Enter":
        print("this thing works\nUsername: " + values[0])
        break
    else:
        curwin.close()
        c.connect.close
        exit()
curwin.close()
layout = [
    [sg.Text("Choose Recipient"), sg.Combo(values=['User1', 'User2'])],
    [sg.Button("button")]
]
curwin = sg.Window("Chats", layout)
event, values = curwin.read()
curwin.close()


c.close()