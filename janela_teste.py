import PySimpleGUI as sg

def janela_inicial():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Get Ready')],
                [sg.Text('00:00')],
                [sg.Button('Play')] ]

    return sg.Window('Inicial', layout=layout, finalize=True)

def janela_focus():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Focus Time')],
                [sg.Text('00:00')],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Focus', layout=layout, finalize=True)

def janela_break():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Break Time')],
                [sg.Text('00:00')],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Break', layout=layout, finalize=True)

janela1, janela2, janela3 = janela_inicial(), None, None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED: 
        break
    if window == janela1 and event == 'Play':
        janela2 = janela_focus()
        janela1.hide()

window.close()