import PySimpleGUI as sg
import controller


def userAcc():
    sg.change_look_and_feel('Reddit')
    layout = [
        [sg.Text('Please enter your User information')],
        [sg.Text('Name', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Username', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Password', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Level', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Submit(), sg.Cancel()]

    ]

    window = sg.Window('Acrolect', layout, grab_anywhere=True)
    button, values = window.Read()

    return values[0], values[1], values[2], values[3]


def studentAcc():
    sg.change_look_and_feel('Reddit')
    layout = [
        [sg.Text('Please enter your User information')],
        [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
        [sg.Text('Username', size=(15, 1)), sg.InputText('username')],
        [sg.Text('Password', size=(15, 1)), sg.InputText('password')],
        [sg.Text('Level', size=(15, 1)), sg.InputText('level')],
        [sg.Submit(), sg.Cancel()]

    ]

    window = sg.Window('Acrolect').Layout(layout)
    button, values = window.Read()

    return values[0], values[1], values[2], values[3]


def teacherAcc():
    sg.change_look_and_feel('Reddit')
    layout = [
        [sg.Text('Please enter your User information')],
        [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
        [sg.Text('Username', size=(15, 1)), sg.InputText('username')],
        [sg.Text('Password', size=(15, 1)), sg.InputText('password')],
        [sg.Text('Level', size=(15, 1)), sg.InputText('level')],
        [sg.Submit(), sg.Cancel()]

    ]

    window = sg.Window('Acrolect').Layout(layout)
    button, values = window.Read()

    return values[0], values[1], values[2], values[3]
