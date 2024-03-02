import httpthingy as c
import PySimpleGUI as sg
import threading
from time import sleep

sg.theme("Black")
connectionSuccess = c.connect()
if connectionSuccess == False:
    layout = [
        [sg.Text("The connection could not establish.")],
        [sg.Ok()]
    ]
    window = sg.Window("Connection Failed", layout)
    event, values = window.read()
    while True:
        if event == "Ok":
            window.close()
            exit()

def login():
    def ev(a):
        layout = [
            [sg.Text(a)],
            [sg.Button("Ok")]
        ]
        win = sg.Window("Error", layout)
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
        [sg.Text("Enter your Password"), sg.InputText(password_char='•')],
        [sg.Button("Login"), sg.Button("Register"), sg.Button("Cancel")]
    ]
    win = sg.Window("Login", layout)
    event, values = win.read()
    while True:
        global username
        username = values[0]
        if event == "Login":
            if values[0] == "":
                win.close()
                ev("Please Enter a Username")
            elif values[1] == "":
                win.close()
                ev("Please Enter a Password")
            print("\nthis thing works")
            loginsuccess = c.passman(values[0], values[1])
            if loginsuccess == "True":
                print("\nLogin Successful")
                break
            else:
                win.close()
                ev("Login Failed")
        elif event == "Register":
            if values[0] == "":
                win.close()
                ev("Please Enter a Username")
            elif values[1] == "":
                win.close()
                ev("Please Enter a Password")
            print("\nRegister time\n")
            a = c.Register(values[0], values[1])
            if a == "uname unav":
                win.close()
                ev("Username Unavailable")
            break
        else:
            win.close()
            c.close()
            exit()
    win.close()
login()

def chat():
    global Running
    Running = True
    ustring = c.getUsers(username)
    ustring = ustring.replace("'", "")
    ulist = ustring.strip("][").split(', ')
    layout = [
        [sg.Text("Chat"), sg.OptionMenu(values=ulist)],
        [sg.Button("Choose")]
    ]
    win = sg.Window("Chats", layout)
    event, values = win.read()
    global recipient
    recipient = values[0]
    while True:
        if event == "Choose" and values[0]:
            print("\nthis guy works too\nChose: " + values[0])
            break
        else:
            win.close()
            c.close()
            Running = False
            exit()
    win.close()
    # def messagePoll():
    #     while Running:
    #         sleep(1)
    #         nonlocal msgHistory
    #         nonlocal msg
    #         a = c.messagePoll(username, recipient)
    #         b = a.replace(msgHistory, '')
    #         msgHistory = a
    #         if b != "":
    #             sg.cprint(b)
    
    # t1 = threading.Thread(messagePoll())
    # t1.start()
    # print("why no worki")
    msg = ""
    msgHistory = c.getMsgHistory(recipient, username)
    layout = [
        [sg.Multiline(size=(100, 70), expand_x=True, expand_y=True, write_only=True, autoscroll=True, reroute_cprint=True, auto_refresh=True)],
        [sg.InputText()],
        [sg.Button("Send")]
    ]
    win = sg.Window("Chats", layout, finalize=True)
    sg.cprint(msgHistory)
    while True:
        event, values = win.read()
        if event == "Send":
            msg = c.send(username, values[1], recipient)
            sg.cprint(msg)
            event = None
        else:
            win.close()
            c.close()
            Running = False
            exit()
chat()

Running = False
c.close()