import httpthingy as c
import PySimpleGUI as sg 
import hashlib

def passcrypt(u, p):
    salt = c.getSalt(u)
    sp = p + salt
    ap = bytes(sp, 'utf-8')
    hashpass = hashlib.sha3_512(ap)
    print(hashpass.hexdigest())

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
            passcrypt(values[0], values[1])
            break
        else:
            win.close()
            c.close()
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