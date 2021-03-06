import PySimpleGUI as sg


class GUI:

    @staticmethod
    def begin():
        sg.change_look_and_feel('Reddit')
        layout = [
            [sg.Text('')],
            [sg.Text('', size=(17, 1)),
             sg.Image(r'C:\Users\tu02_\PycharmProjects\ICS4U-EnglishApplication\logo(5).png')],
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
                window.close()
                return True, values['USERNAME'], values['PASSWORD']
            elif event == 'Create account':
                window.close()
                return False

    @staticmethod
    def displayInfo(userInfo, personalInfo):
        sg.change_look_and_feel('Reddit')

        menu_def = [

            ['File', ['Account', ['Open', ['User Info', 'Personal Info', 'Document']]], 'Save', 'Exit'],
            ['View', ['Flesh score']],
            ['Help', ['About']]

        ]

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
                viewInfo = ('----------------View Info----------------\n' + 'Name: ' + userInfo[0] + '\n' + 'User: ' +
                            userInfo[1] + '\n' + 'Password: ' + userInfo[2] + '\n' + 'Occupation: ' + userInfo[
                                3] + '\n')
                print(viewInfo)

            elif event == 'Personal Info':
                studentView = ('--------------Personal Info--------------\n' + 'Name: ' + personalInfo[0] + '\n' +
                               'User: ' + personalInfo[1] + '\n' + 'Password: ' +
                               personalInfo[2] + '\n' + 'Occupation: ' + personalInfo[3] + '\n' + 'School: ' +
                               personalInfo[3] + '\n' + 'Course: ' + personalInfo[3] + '\n' + 'Grade: ' +
                               personalInfo[3] + '\n' + 'Age: ' + personalInfo[3] + '\n' + 'Reading Level: ' +
                               personalInfo[4] + '\n')
                print(studentView)

            elif event == 'Flesch score':
                return 'Flesch score'

            elif event == 'Document':
                return 'Document'

            elif event == 'About':
                sg.popup_get_text('For more information about this program please visit the Github page using this '
                                  'link:', default_text='https://github.com/KevinT02/ICS4U-EnglishApplication',
                                  size=(50, 1),
                                  title='Github Link')

    @staticmethod
    def popFile(fileContent):
        layout = [

            [sg.Output(size=(80, 18))],
            [sg.Button('Display'), sg.Button('Close')]

        ]

        window = sg.Window('Document', layout)

        while True:
            event, values = window.read()
            if event == 'Display':
                print(fileContent)

            if event == 'Close':
                window.close()
                return 'Close'

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
        layout = [[sg.Image(r'C:\Users\tu02_\PycharmProjects\ICS4U-EnglishApplication\logo(5).png'), sg.Column(col)]]

        window = sg.Window('Create account', layout)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            print(values['NAME'], values['USERNAME'], values['PASSWORD'], values['OCCUPATION'])
            if event in (None, 'Cancel'):
                window.close()
                break
            elif event == 'Submit':
                if values['NAME'] != '' and values['USERNAME'] != '' and values['PASSWORD'] != '' and \
                        values['OCCUPATION'] != '':

                    if values['OCCUPATION'] == 'Student' or values['OCCUPATION'] == 'Teacher':
                        window.close()

                        return values['NAME'], values['USERNAME'], values['PASSWORD'], values['OCCUPATION']

                    else:
                        sg.popup('Occupation invalid, use the drop down menu')

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
            [sg.Text('Reading Level', size=(15, 1)),
             sg.Slider(range=(1, 10), orientation='h', size=(30, 16), key='LEVEL')],
            [sg.Submit(), sg.Cancel()]

        ]

        window = sg.Window('Student Account Setup').Layout(layout)
        button, values = window.Read()
        if button == "Submit" or button == "Cancel":
            window.close()

        return values['SCHOOL'], values['COURSE'], values['GRADE'], values['AGE'], str(values['LEVEL'])

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

        if button == "Submit" or button == "Cancel":
            window.close()

        return values['DEGREE'], values['SCHOOL'], values['COURSE'], values['EXPERIENCE']

    @staticmethod
    def incorrectPopup():
        sg.popup('The password or username does not match or exist. Please try again')
