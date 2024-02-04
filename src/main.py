import httpthingy as c
import PySimpleGUI as sg 

c.connect()
sg.theme("Black")

def login():
    def ev(a):
        layout = [
            [sg.Text(a)],
            [sg.Button("Ok")]
        ]
        win = sg.Window("Error", layout)
        event, values= win.read()
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
    global username
    username = values[0]
    while True:
        if event == "Login":
            if values[0] == "":
                win.close()
                ev("Please Enter a Username")
            elif values[1] == "":
                win.close()
                ev("Please Enter a Password")
            print("\nthis thing works\nUsername: " + values[0] + "\nPass: " + values[1])
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
    ustring = c.getUsers(username)
    ustring = ustring.replace("'", "")
    ulist = ustring.strip("][").split(', ')
    layout = [
        [sg.Text("Chat"), sg.Combo(values=ulist)],
        [sg.Button("Choose")]
    ]
    win = sg.Window("Chats", layout)
    event, values = win.read()
    global recipient
    recipient = values[0]
    while True:
        if event == "Choose" and values[0]:
            print("\nthis guy works too\nChose: " + values[0])
            c.recip(values[0])
            break
        else:
            win.close()
            c.close()
            exit()
    win.close()
    layout = [
        [sg.Multiline(size=(100, 70), expand_x=True, expand_y=True, write_only=True, autoscroll=True, auto_refresh=True)],
        [sg.InputText()],
        [sg.Button("Send")]
    ]
    win = sg.Window("Chats", layout)
    while True:
        event, values = win.read()
        if event == "Send":
            print(values)
            c.send(username, values[1], recipient)
            event = None
        else:
            win.close()
            c.close()
            exit()
chat() 

c.close()