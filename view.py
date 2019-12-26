import PySimpleGUI as sg


class GUI:

    @staticmethod
    def begin():
        sg.change_look_and_feel('Reddit')
        layout = [
            [sg.Text('')],
            [sg.Text('', size=(17, 1)),
             sg.Image(r'C:\Users\Kevin\PycharmProjects\ICS4U-EnglishApplication\logo(5).png')],
            [sg.Text('Sign in', size=(45, 2), font=('Helvetica', 15), justification='left')],
            [sg.Text('Username'), sg.Input(size=(45, 1))],
            [sg.Text('Password'), sg.Input(size=(45, 1))],
            [sg.Text('')],
            [sg.Button('Login'), sg.Button('Create account')]

        ]

        window = sg.Window('Main Menu', layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)

            if event in (None, 'Cancel'):
                break
            elif event == 'Create account':
                window.close()
                return

    @staticmethod
    def userAcc():
        sg.change_look_and_feel('Reddit')

        # Column layout
        col = [
            [sg.Text('Please fill in the following:', size=(40, 2), font=('Helvetica', 12))],
            [sg.Text('Name', size=(15, 1)),
             sg.Input(size=(45, 1), key='NAME')],
            [sg.Text('Username', size=(15, 1)),
             sg.Input(size=(45, 1), key='USERNAME')],
            [sg.Text('Password', size=(15, 1)),
             sg.Input(size=(45, 1), password_char='•', key='PASSWORD'),
             sg.Button('Show')],
            [sg.Text('Level', size=(15, 1)),
             sg.DropDown(('Student', 'Teacher'), size=(40, 1), key='OCCUPATION')],
            [sg.Text('')],
            [sg.Submit(), sg.Cancel()]]

        # Main layout
        layout = [[sg.Image(r'C:\Users\Kevin\PycharmProjects\ICS4U-EnglishApplication\logo(5).png'), sg.Column(col)]]

        window = sg.Window('Create account', layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            print(values['NAME'], values['USERNAME'], values['PASSWORD'], values['OCCUPATION'])
            if event in (None, 'Cancel'):
                window.close()
                break
            elif event == 'Submit':
                if values['NAME'] != '' and values['USERNAME'] != '' and values['PASSWORD'] != '' and values[
                    'OCCUPATION'] != '':

                    if values['OCCUPATION'] == 'Student' or values['OCCUPATION'] == 'Teacher':
                        window.close()

                        return values['NAME'], values['USERNAME'], values['PASSWORD'], values['OCCUPATION']

                    else:
                        sg.popup('Occupation invalid, use the dropdown menu')

                else:
                    sg.popup('Please fill in all boxes')
            elif event == 'Show':
                sg.popup(values['PASSWORD'])

    @staticmethod
    def studentAcc():
        sg.change_look_and_feel('Reddit')
        layout = [
            [sg.Text('Student Account Setup', size=(40, 2), font=('Helvetica', 25))],
            [sg.Text('Please enter your User information')],
            [sg.Text('Course', size=(15, 1)), sg.Input(size=(45, 1))],
            [sg.Text('Grade', size=(15, 1)), sg.Input(size=(45, 1))],
            [sg.Text('Age', size=(15, 1)), sg.Input(size=(45, 1))],
            [sg.Text('Reading Level', size=(15, 1)), sg.Input(size=(45, 1))],
            [sg.Submit(), sg.Cancel()]

        ]

        window = sg.Window('Student Account Setup').Layout(layout)
        button, values = window.Read()

        return values[0], values[1], values[2], values[3]

    @staticmethod
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
