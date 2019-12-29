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
            [sg.Text('Username'), sg.Input(size=(45, 1), key='USERNAME')],
            [sg.Text('Password'), sg.Input(size=(45, 1), key='PASSWORD')],
            [sg.Text('')],
            [sg.Button('Login'), sg.Button('Create account')]

        ]

        window = sg.Window('Home Page', layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)

            if event in (None, 'Cancel'):
                break
            elif event == 'Login':
                return True, values['USERNAME'], values['PASSWORD']
            elif event == 'Create account':
                window.close()
                return False

    @staticmethod
    def displayInfo(userInfo, personalInfo):
        sg.change_look_and_feel('Reddit')

        menu_def = [['File', ['Open', ['User Info', 'Personal Info'], 'Save', 'Exit', 'Properties']],
                    ['Edit', ['Paste', ['Normal'], 'Undo']],
                    ['Help', 'About'], ]

        layout = [
            [sg.Menu(menu_def, tearoff=True)],
            [sg.Text('Account Info', size=(35, 2), font=('Helvetica', 20), justification='left')],
            [sg.Output(size=(80, 18))],
            [sg.Text('')],
            [sg.Button('Exit')]

        ]
        window = sg.Window('Account Info', layout)

        # ------ Loop & Process button menu choices ------ #
        while True:
            event, values = window.read()
            if event is None or event == 'Exit':
                break
            # ------ Process menu choices ------ #
            if event == 'About...':
                sg.popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
            elif event == 'User Info':
                print(userInfo)

            if event == 'personalInfo':
                print(personalInfo)


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
             sg.InputOptionMenu(('Student', 'Teacher'), size=(40, 1), key='OCCUPATION')],
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
            [sg.Text('Please fill in the following:')],
            [sg.Text('School', size=(15, 1)), sg.Input(size=(45, 1), key='SCHOOL')],
            [sg.Text('Course', size=(15, 1)), sg.Input(size=(45, 1), key='COURSE')],
            [sg.Text('Grade', size=(15, 1)), sg.Input(size=(45, 1), key='GRADE')],
            [sg.Text('Age', size=(15, 1)), sg.Input(size=(45, 1), key='AGE')],
            [sg.Text('Reading Level', size=(15, 1)), sg.Input(size=(45, 1), key='LEVEL')],
            [sg.Submit(), sg.Cancel()]

        ]

        window = sg.Window('Student Account Setup').Layout(layout)
        button, values = window.Read()

        return values['SCHOOL'], values['COURSE'], values['GRADE'], values['AGE'], values['LEVEL']

    @staticmethod
    def teacherAcc():
        sg.change_look_and_feel('Reddit')
        layout = [
            [sg.Text('Teacher Account Setup', size=(40, 2), font=('Helvetica', 25))],
            [sg.Text('Please fill in the following:')],
            [sg.Text('Degree', size=(15, 1)), sg.Input(size=(45, 1), key='DEGREE')],
            [sg.Text('School', size=(15, 1)), sg.Input(size=(45, 1), key='SCHOOL')],
            [sg.Text('Course', size=(15, 1)), sg.Input(size=(45, 1), key='COURSE')],
            [sg.Text('Experience', size=(15, 1)), sg.Input(size=(45, 1), key='EXPERIENCE')],
            [sg.Submit(), sg.Cancel()]

        ]

        window = sg.Window('Teacher Account Setup').Layout(layout)
        button, values = window.Read()

        return values['DEGREE'], values['SCHOOL'], values['COURSE'], values['EXPERIENCE']
