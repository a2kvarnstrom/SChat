import httpthingy as c
import PySimpleGUI as sg 

c.connect()
sg.theme("Black")

def login():
    layout = [
        [sg.Text("Enter your Username"), sg.InputText()],
        [sg.Text("Enter your Password"), sg.InputText()],
        [sg.Button("Login"), sg.Button("Register"), sg.Button("Cancel")]
    ]
    win = sg.Window("Login", layout)
    event, values = win.read()
    while True:
        if event == "Login":
            print("\nthis thing works\nUsername: " + values[0] + "\nPass: " + values[1])
            loginsuccess = c.passman(values[0], values[1])
            if loginsuccess == "True":
                print("yay")
                break
            else:
                print("nay")
                win.close()
                layout = [
                    [sg.Text("Invalid Username")],
                    [sg.Button("Ok")]
                ]
                win = sg.Window("Login", layout)
                event, values = win.read()
                while True:
                    if event == "Ok":
                        win.close()
                        break
                    else:
                        win.close()
                        break
                login()
        elif event == "Register":
            print("\nRegister time\n")
            c.Register(values[0], values[1])
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
        if event == "Choose" and values[0]:
            print("\nthis guy works too\nChose: " + values[0])
            break
        else:
            win.close()
            c.close()
            exit()
    win.close()
recip()

c.close()