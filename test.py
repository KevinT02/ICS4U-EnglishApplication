import PySimpleGUI as sg

'''
# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.

window = sg.Window('Columns')                                   # blank window

# Column layout
col = [[sg.Text('col Row 1')],
       [sg.Text('col Row 2'), sg.Input('col input 1')],
       [sg.Text('col Row 3'), sg.Input('col input 2')],
       [sg.Text('col Row 4'), sg.Input('col input 3')],
       [sg.Text('col Row 5'), sg.Input('col input 4')],
       [sg.Text('col Row 6'), sg.Input('col input 5')],
       [sg.Text('col Row 7'), sg.Input('col input 6')]]

layout = [[sg.Image(r'C:\Users\Kevin\PycharmProjects\ICS4U-EnglishApplication\logo(2).png'), sg.Column(col)],
          [sg.In('Last input')],
          [sg.OK()]]
# Display the window and get values

window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.Close()

sg.Popup(event, values, line_width=200)
'''

sg.change_look_and_feel('Reddit')

layout = [
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


window = sg.Window('User Login', layout)
event, values = window.read()
print(values[])
