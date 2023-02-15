import PySimpleGUI as sg
import time
init_temp = time.time()

def pausa_c():
    init_temp = time.time()
    print('Pausa curta')
    while True:
        contador = int(time.time() - init_temp)
        if contador == p_curta:
            print('Acabou a Pausa')
            break
        else:
            print(contador)
            time.sleep(1)
    return

def pausa_l():
    init_temp = time.time()
    print('Pausa longa')
    while True:
        contador = int(time.time() - init_temp)
        if contador == p_longa:
            print('Acabou a Pausa')
            break
        else:
            print(contador)
            time.sleep(1)
    return

def prin():
    while True:
        contador = int(time.time() - init_temp)
        if  pausas == 4 and contador == timer:
            pausa_l()
            pausas = 0
            init_temp = time.time()
        elif contador == timer:
            pausa_c()
            pausas += 1
            init_temp = time.time()
        else:
            print(contador)
            time.sleep(1)
    return


def janela_inicial():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Get Ready')],
                [sg.InputText(size=(10,1), key='timer')],
                [sg.Button('Play')] ]

    return sg.Window('Inicial', layout=layout, finalize=True)

def janela_focus():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Focus Time')],
                [sg.Text(time.time())],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Focus', layout=layout, finalize=True)

def janela_break():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Break Time')],
                [sg.Text('00:00')],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Break', layout=layout, finalize=True)

p_curta = 5*60
p_longa = 15*60
pausas = 0

janela1, janela2, janela3 = janela_inicial(), None, None
timer = None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED: 
        break
    if window == janela2 and event == sg.WIN_CLOSED: 
        break
    if window == janela1 and event == 'Play':
        janela1.hide()
        janela2 = janela_focus()
        
window.close()