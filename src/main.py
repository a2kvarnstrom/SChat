import httpthingy as c
import PySimpleGUI as sg 
import bcrypt

def passcrypt(p, u):
    salt = c.getSalt(u)
    hashpass = bcrypt.hashpw(p, salt)
   
c.connect()
sg.theme("Black")

def login():
    layout = [
        [sg.Text("Enter your Username"), sg.InputText()],
        [sg.Text("Enter your Password"), sg.InputText()],
        [sg.Button("Enter"), sg.Button("Cancel")]
    ]
    win = sg.Window("Login", layout)
    event, values = win.read()
    while True:
        if event == "Enter":
            print("\nthis thing works\nUsername: " + values[0] + "\nPass: " + values[1])
            break
        else:
            win.close()
            c.connect.close
            exit()
    win.close()
login()

def recip():
    layout = [
        [sg.Text("Choose Recipient"), sg.Combo(values=['User1', 'User2'])],
        [sg.Button("Choose")]
    ]
    win = sg.Window("Chats", layout)
    event, values = win.read()
    while True:
        if event == "Choose":
            print("\nthis guy works too\nChose: " + values[0])
            break
    win.close()
recip()

c.close()