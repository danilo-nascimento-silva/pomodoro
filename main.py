from tkinter import *
import time

timer = float(input('Digite quantidade de tempo em minutos: '))
timer = int(timer*60)
p_curta = 5*60
p_longa = 15*60
contador = 0

janela = Tk()
janela.title('Pomodoro')
janela.geometry('950x350+500+200')
janela.resizable(False, False)
janela.iconbitmap("imagens/pomodoro_icon.ico")
janela['bg'] = '#97CDB5'
photo = PhotoImage(file='imagens/tomate.png')

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

def play():
    init_temp = time.time()
    pausas = 0
    while True:
        global contador
        contador = int(time.time() - init_temp)
        if  pausas == 2 and contador == timer:
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

print(contador)       
# botao_play = Button(janela, text='Play', command=play,width=10, height=2, bg='#FF6242', fg='white', font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
# botao_play.place(x=650, y=270)
# botao_pause = Button(janela, text='Pause', width=10, height=2, bg='#FF6242', fg='white', font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
# botao_pause.place(x=770, y=270)
# label_relogio = Label(janela, text=contador, font=('Times 150 bold'), fg='#DB524D', bg='#97CDB5')
# label_relogio.place(x=50,y=50)

janela.mainloop()