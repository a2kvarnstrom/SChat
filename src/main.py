import httpthingy as c
import PySimpleGUI as sg 

c.connect()
sg.theme("Black")

def login():
    def ep():
        layout = [
                    [sg.Text("Please Enter a password")],
                    [sg.Button("Ok")]
                ]
        win = sg.Window("No Password", layout)
        event, values = win.read()
        while True:
            if event == "Ok":
                win.close()
                break
            else:
                win.close()
                break
        login()
    def eu():
        layout = [
            [sg.Text("Please Enter a username")],
            [sg.Button("Ok")]
        ]
        win = sg.Window("No Username", layout)
        event, values = win.read()
        while True:
            if event == "Ok":
                win.close()
                break
            else:
                win.close()
                break
        login()
    def iu():
        layout = [
            [sg.Text("Invalid Username")],
            [sg.Button("Ok")]
        ]
        win = sg.Window("Invalid Username", layout)
        event, values = win.read()
        while True:
            if event == "Ok":
                win.close()
                break
            else:
                win.close()
                break
        login()
    layout = [
        [sg.Text("Enter your Username"), sg.InputText()],
        [sg.Text("Enter your Password"), sg.InputText()],
        [sg.Button("Login"), sg.Button("Register"), sg.Button("Cancel")]
    ]
    win = sg.Window("Login", layout)
    event, values = win.read()
    global username
    username = values[0]
    while True:
        if event == "Login":
            if values[0] == "":
                win.close()
                eu()
            elif values[1] == "":
                win.close()
                ep()
            print("\nthis thing works\nUsername: " + values[0] + "\nPass: " + values[1])
            loginsuccess = c.passman(values[0], values[1])
            if loginsuccess == "True":
                print("\nLogin Successful")
                break
            else:
                print("nay")
                win.close()
                iu()
        elif event == "Register":
            if values[0] == "":
                win.close()
                eu()
            elif values[1] == "":
                win.close()
                ep()
            print("\nRegister time\n")
            a = c.Register(values[0], values[1])
            if a == "uname unav":
                win.close()
                iu()
            break
        else:
            win.close()
            c.close()
            exit()
    win.close()
login()

def chat():
    ustring = c.getUsers(username)
    ustring = ustring.replace("'", "")
    ulist = ustring.strip("][").split(', ')
    layout = [
        [sg.Text("Chat"), sg.Combo(values=ulist)],
        [sg.Button("Choose")]
    ]
    win = sg.Window("Chats", layout)
    event, values = win.read()
    while True:
        if event == "Choose" and values[0]:
            print("\nthis guy works too\nChose: " + values[0])
            break
        else:
            win.close()
            c.close()
            exit()
    win.close()
chat() 

c.close()