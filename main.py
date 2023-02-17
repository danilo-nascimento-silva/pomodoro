import PySimpleGUI as sg #Biblioteca para interface 
import time #Biblioteca para contar tempo
# ------------------------------------ Função que mantém a pagina inicial ------------------------------------
def janela_inicial():
    sg.theme('Reddit')   # Tema da pagia
    layout = [  [sg.Text('Get Ready')], # Nome topo da pagina
                [sg.InputText(size=(10,1), key='timer_')], # Caixa de texto que recebe a quantidade de tempo
                [sg.Button('Play')] ] # Botão para o iniciar 

    return sg.Window('Inicial', layout=layout, finalize=True)
# ------------------------------------ Função que mantém a pagina de foco ------------------------------------
def janela_focus():
    sg.theme('DarkRed2')   # Tema da pagia
    layout = [  [sg.Text('Focus Time')], # Nome topo da pagina
                [sg.Text(t)], # Texto que recebe a variável de tempo 
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ] # Botões de Play, pause e Restart 

    return sg.Window('Focus', layout=layout, finalize=True)
# ------------------------------------ Função que mantém a pagina de descanso ------------------------------------
def janela_break():
    sg.theme('DarkGreen')   # Tema da pagia
    layout = [  [sg.Text('Break Time')], # Nome topo da pagina
                [sg.Text(t)], # Texto que recebe a variável de tempo 
                [sg.Button('Play'), sg.Button('Pause'), sg.Button('Restart')] ] # Botões de Play, pause e Restart 

    return sg.Window('Break', layout=layout, finalize=True)

janela1, janela2, janela3 = janela_inicial(), None, None # Variáveis que recebe as paginas 

t = 0 # Declarar a variável de tempo que é atualizada no loop 
pomodoro = t # Guarda o tempo desejado 
pausa_c = 5 #300 5 minutos para a pausa curta
pausa_l = 10 #1200 15 minutos para a pausa longa
pausas = 0  # Variável que armazena a quantidade de pausas curta para chamar a pausa longa
mudar_tela = False # Variével que muda a tela nas pausas

while True:

    window, event, values = sg.read_all_windows() 
# ------------------------------------ Condições que verifica se a aplicação foi fechada ------------------------------------

    if window == janela1 and event == sg.WIN_CLOSED: 
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break 
    if window == janela3 and event == sg.WIN_CLOSED:
        break 

# ---------------------------------------------------------------------------------------------------------------------------

    if window == janela1 and event == 'Play': # Condição que verifica se a janela de apresentação esta aberta e se o botão play foi pressionado
        janela1.hide() # Fecha a janela de apresentação
        janela2 = janela_focus() # Abre a janela de Foco 
        t = int(values['timer_'])*60 # Atribui a variavel "t" o valor digitado na tela de apresentação 
        pomodoro = int(t) # Guarda o valor atribuído em outra variável para salvar a informação e usar no término do loop de pausa

    if window == janela2 and event == 'Restart': # Verifica se o botão de restart foi pressionado na tela de foco
        print('Reset')
        t = pomodoro # Reseta o tempo, atribuído o valor que foi salvo na variavel Pomodoro 

    if window == janela2 and mudar_tela: # Verifica se a janela de foco esta aberta e se a variável for True
        janela2.hide() # Fecha a janela de foco
        janela3 = janela_break() # Abre a janela de pausa

    minutes, seconds = divmod(t, 60) # Recebe a informação de tempo em segundos, divide para transformar de segundos para minutos e atribui o- 
    # valor da divisão inteira para a variável "Minutos" e o resto da divisão para a variével "Segundos"
    timer = "{:02d}:{:02d}".format(minutes, seconds) # Monta o formato de print para ser impresso
    print(timer, end="\r") # Printa a variável s
    t -= 1 # A cada segundo decrementa 1 segundo da variável "t"
    time.sleep(1) # Segura o codigo por 1 segundo 

    if t == 0 and pausas == 4: # Condição que verifica se a variável "t" chegou a zero e se a variável pausas chegou a 4
        # isso significa que ja tiveram 4 pausas curtas e ta na hora que chamar uma pausa longa
        print('Pausa Longa')
        pausas = 0 # Zera a quantidade de pausas 
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

    if t == 0: # Condição que verifica se a variável "t" chegou a zero para chamar uma pausa curta
        print('Pausa Curta')
        pausas += 1 # Atribui +1 na variavel para verificar se esta na hora de uma pausa longa
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

