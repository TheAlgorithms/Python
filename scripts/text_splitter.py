import PySimpleGUI as sg
splitted = ""
text = ""
sg.theme('DarkBlue4')
layout = [[sg.Text('Text for splitting'), sg.InputText(size=(20, 5), key='input')],
            [sg.Text('How many symbols in one part'),sg.InputText(size=(5, 1), key='symbols'),sg.Text('(Count on additional symbols for amount of parts)')],
            [sg.Checkbox('Do we add amount of parts?', key='split')], 
            [sg.Button('Split')],
            [sg.Multiline(splitted, key='-logtext-', size =(None, 10), rstrip=False)], [sg.Button('Clear'), sg.Text('                                                © @uahave.fun', text_color='dark blue', font=('Helvetica', 10), justification='right')],[sg.Text('------------------------------------------------------')],[sg.Button('Close')]
            ]

window = sg.Window('Splitter', layout)

while True:
    event, values = window.read()
    if event in (None, 'Close'):
        break
    if event == 'Split':
        if values['input'] == '':
            sg.popup('Add text to split!')
            continue
        if values['symbols'].isdigit() == False:
            sg.popup('Symbols amount must be numeric only!')
            continue
        if values['symbols'] == '':
            sg.popup('Enter symbols amount!')
            continue
        if int(values['symbols']) < 1:
            sg.popup('Enter symbols amount > 0!')
            continue
        if int(values['symbols']) > len(values['input']):
            sg.popup('Enter symbols amount less then whole text size!')
            continue
        if int(values['symbols']) == len(values['input']):
            sg.popup('Enter symbols amount less then whole text size!')
            continue
        es = [values['input'][i:i + int(values['symbols'])] for i in range(0, len(values['input']), int(values['symbols']))] 
        for i in es:
            if values['split'] == True:
                text =  text + str(es.index(i)+1) + '/' + str(len(es))+ ' ' + splitted + i +  '\n' + '\n'
            else:
                text = text + splitted + i + '\n' + '\n'
        window['-logtext-'].update(text)
    if event == 'Clear':
        window['-logtext-'].update('')
        text = ''
window.close()

