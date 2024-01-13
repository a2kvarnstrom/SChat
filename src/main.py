import httpthingy as c
import PySimpleGUI as sg 

c.connect()

sg.theme("DarkAmber")
layout = [
    [sg.Text("Enter your Username"), sg.InputText()],
    [sg.Button("Enter"), sg.Button("Cancel")]
]
curwin = sg.Window("Login", layout)
event, values = curwin.read()
while True:
    if event == "Enter":
        print("this thing works")
        break
    else:
        curwin.close()
curwin.close()
layout = [
    [sg.Text("Choose Recipient"), sg.ButtonMenu("Button1", ['Menu', ['&Pause Graph', 'Menu item::optional_key']])],
    [sg.Button("button")]
]
curwin = sg.Window("Chats", layout)
event, values = curwin.read()
curwin.close()


c.connect.close