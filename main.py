import PySimpleGUI as sg
import time

def janela_inicial():
    sg.theme('Reddit')   
    layout = [  [sg.Text('Get Ready')],
                [sg.InputText(size=(10,1), key='timer_')],
                [sg.Button('Play')] ]

    return sg.Window('Inicial', layout=layout, finalize=True)

def janela_focus():
    sg.theme('DarkRed2')   
    layout = [  [sg.Text('Focus Time')],
                [sg.Text(t)],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Focus', layout=layout, finalize=True)

def janela_break():
    sg.theme('DarkGreen')   
    layout = [  [sg.Text('Break Time')],
                [sg.Text('00:00')],
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ]

    return sg.Window('Break', layout=layout, finalize=True)

janela1, janela2, janela3 = janela_inicial(), None, None

t = 0
pomodoro = t # Guarda o tempo desejado 
pausa_c = 5 #300 5 minutos para a pausa curta
pausa_l = 10 #1200 15 minutos para a pausa longa
pausas = 0
mudar_tela = False



while True:
    window, event, values = sg.read_all_windows() 

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break 
    if window == janela3 and event == sg.WIN_CLOSED:
        break 

    if window == janela1 and event == 'Play':
        janela1.hide()
        janela2 = janela_focus()
        t = int(values['timer_'])*60
        pomodoro = int(t)
    if window == janela2 and event == 'Restart':
        print('Reset')
        t = pomodoro
    if window == janela2 and mudar_tela:
        janela2.hide()
        janela3 = janela_focus()

    minutes, seconds = divmod(t, 60)    
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    t -= 1
    time.sleep(1)

    if t == 0 and pausas == 4:
        print('Pausa Longa')
        pausas = 0
        mudar_tela = True  
        while pausa_l != 0:
            minutes, seconds = divmod(pausa_l, 60)    
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            pausa_l -= 1
        print('Acabou a pausa curta')
        t = pomodoro
        mudar_tela = False 

    if t == 0:
        print('Pausa Curta')
        pausas += 1
        mudar_tela = True   
        while pausa_c != 0:
            minutes, seconds = divmod(pausa_c, 60)    
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            pausa_c -= 1
        print('Acabou a pausa curta')
        t = pomodoro
        mudar_tela = False

