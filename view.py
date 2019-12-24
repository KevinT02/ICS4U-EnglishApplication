import PySimpleGUI as sg
import controller


def begin():
    sg.change_look_and_feel('Reddit')
    layout = [
        [sg.Text('')],
        [sg.Text('Acrolect', size=(8, 2), font=('Helvetica', 20), justification='left')],
        [sg.Text('Please enter your User information')],
        [sg.Text('Name', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Username', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Password', size=(15, 1)),
         sg.Input(size=(45, 1), password_char='•')],
        [sg.Text('Level', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Submit(), sg.Cancel()]

    ]

    window = sg.Window('User Login', layout)
    button, values = window.Read()

    return


def userAcc():
    sg.change_look_and_feel('Reddit')

    # Column layout
    col = [
        [sg.Text('Please enter your User information', size=(25, 1))],
        [sg.Text('Name', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Username', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Text('Password', size=(15, 1)),
         sg.Input(size=(45, 1), password_char='•'),
         sg.Button('Show')],
        [sg.Text('Level', size=(15, 1)),
         sg.Input(size=(45, 1))],
        [sg.Submit(), sg.Cancel()]]

    layout = [[sg.Image(r'C:\Users\Kevin\PycharmProjects\ICS4U-EnglishApplication\logo(2).png'), sg.Column(col)]]

    window = sg.Window('User Login', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        print(values[1], values[1], values[2], values[3])
        if event in (None, 'Cancel'):
            break
        if event == 'Submit':
            return values[1], values[1], values[2], values[3]
        if event == 'Show':
            sg.popup(values[2])
    return


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
