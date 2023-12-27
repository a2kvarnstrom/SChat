import PySimpleGUI as sg
import chatlib as chat

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


layout = [
    [sg.Text("Who do you Want to chat with?")]
    [sg.Button("")]
]