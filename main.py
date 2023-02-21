import PySimpleGUI as sg #Biblioteca para interface 
import time #Biblioteca para contar tempo
import winsound

# Verifica se a string representa um inteiro

def isInt(value):
    value_int = None
    try:
        value_int = int(value)
        if value_int is not None:
            return True
    except:
        return False

# Função que emite um som de alerta 

def alarme():
    winsound.MessageBeep(type=-1)

# Função que mantém a pagina inicial

def janela_inicial():
    sg.theme('Reddit')   # Tema da pagia
    layout = [  [sg.Text('Get Ready')], # Nome topo da pagina
                [sg.Text('Tempo de Foco:  '), sg.InputText(size=(9,1), key='timer_')], # Caixa de texto que recebe a quantidade de tempo
                #[sg.Text('Pausa Curta:      '), sg.InputText(size=(9,1), key='focus_c')],
                #[sg.Text('Pausa Longa:     '), sg.InputText(size=(9,1), key='focus_l')], # Caixa de texto que recebe a quantidade de tempo
                [sg.Button('Play', size=(22, 1))] ] # Botão para o iniciar 

    return sg.Window('Inicial', layout=layout, finalize=True)

# Função que mantém a pagina de foco 

def janela_focus(t_, p_):
    sg.theme('DarkRed2')   # Tema da pagia
    layout = [  [sg.Text('Focus Time               '), (sg.Text(p_, key='qtd_focus'))], # Nome topo da pagina
                [sg.Text(t_, key='time_focus_')], # Texto que recebe a variável de tempo 
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ] # Botões de Play, pause e Restart 

    return sg.Window('Focus', layout=layout, finalize=True)

# Função que mantém a pagina de descanso

def janela_break(p_, q):
    sg.theme('DarkGreen')   # Tema da pagia
    layout = [  [sg.Text('Break Time     '), (sg.Text(q, key='qtd_focus'))], # Nome topo da pagina
                [sg.Text(p_, key='time_pause_')], # Texto que recebe a variável de tempo 
                [sg.Button('Play', size=(15, 1))]] # Botão de Play

    return sg.Window('Break', layout=layout, finalize=True)

# Função que converte o tempo de segundos para minutos e formata a saída

def convert_temp(i):
    minutos, segundos = divmod(i, 60)
    return"{:02d}:{:02d}".format(minutos, segundos)

janela1, janela2, janela3 = janela_inicial(), None, None # Variáveis que recebe as paginas 

t = 0 # guarda o tempo de foco no decorrer do código
p = 0 # guarda o tempo de pausa no decorrer do código
quant_p = 0 # Guarda a quantidade de ciclos para diferenciar de pausa curta ou longa
pomodoro = 0 # Guarda o tempo inicial configurado para foco 

flag_decrement_time_focus = False
time_init_focus = None

flag_decrement_time_pause = False
time_init_pause = None

last_window = None


while True:

    window, event, values = sg.read_all_windows(timeout=100)

    if window is not None:
        last_window = window
    else: 
        window = last_window

# ------------------------------------ Condições que verifica se a aplicação foi fechada ------------------------------------

    if window == janela1 and event == sg.WIN_CLOSED: 
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        janela1.un_hide()
        janela2.close() 
        flag_decrement_time_focus = False

    if window == janela3 and event == sg.WIN_CLOSED:
        janela1.un_hide()
        janela3.close() 
        flag_decrement_time_focus = False

    if window == janela3 and event == 'Play':
        time_init_pause = time.time() # Salva o start
        flag_decrement_time_pause = True # Flag que diz que a contagem está habilitada
        p = int(window['time_pause_'].get())
    
    if window == janela1 and event == 'Play': # Condição que verifica se a janela de apresentação esta aberta e se o botão play foi pressionado
        if isInt(values['timer_']):
            if int(values['timer_']) <= 60:
                janela1.hide() # Oculta a janela de apresentação
                t = int(values['timer_'])*60 # Atribui a variavel "t" o valor digitado na tela de apresentação 
                janela2 = janela_focus(t, quant_p) # Abre a janela de Foco e passa o tempo como parâmetro
                pomodoro = t # Guarda o valor atribuído em outra variável para salvar a informação e usar no término do loop de pausa

    if window == janela2 and event == 'Restart': # Verifica se o botão de restart foi pressionado na tela de foco
        window['time_focus_'].update(pomodoro) # Reseta o tempo, atribuído o valor que foi salvo na variavel Pomodoro 
        flag_decrement_time_focus = False

    if window == janela2 and event == 'Play': # Se play, habilita decrementar tempo de foco
        time_init_focus = time.time() # Salva o start
        flag_decrement_time_focus = True # Flag que diz que a contagem está habilitada
        t = int(window['time_focus_'].get())
    
    if window == janela2 and event == 'Pause': 
        flag_decrement_time_focus = False # Flag que diz que a contagem está desabilitada
    
    if flag_decrement_time_focus:
        running_time = int(time.time() -time_init_focus)
        window['time_focus_'].update(convert_temp(t - running_time))
            
        if t -running_time < 0:
            janela2.close()
            alarme()
            if quant_p == 3:
                janela3 = janela_break(900, quant_p)
                quant_p = 0
            else:
                janela3 = janela_break(300, quant_p)
            quant_p += 1
            flag_decrement_time_focus = False
    
    if flag_decrement_time_pause:
        running_time = int(time.time() -time_init_pause)
        window['time_pause_'].update(convert_temp(p -running_time))
            
        if p -running_time < 0 :
            janela3.close()
            janela2 = janela_focus(pomodoro, quant_p)
            flag_decrement_time_pause = False





