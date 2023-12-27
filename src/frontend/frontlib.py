import PySimpleGUI as sg
import sys
sys.path.append("C:/Users/a2kva/Documents/GitHub/SChat/src/backend")
import chatlib as chat

def login():

    sg.theme("DarkAmber")

    layout = [
        [sg.Text("Enter your Username"), sg.InputText()],
        [sg.Button("Enter"), sg.Button("Cancel")]
    ]

    loginWindow = sg.Window("Login", layout)

    event, values = loginWindow.read()

    while True:
        if event == "Enter":
            chat.login(values[0])
            break
    loginWindow.close()