from tkinter import *
import tkinter
import time

janela = Tk()
janela.title('Pomodoro')
janela.geometry('950x350+500+200')
janela.resizable(False, False)
janela.iconbitmap("imagens/pomodoro_icon.ico")
janela['bg'] = '#97CDB5'
photo = PhotoImage(file='imagens/tomate.png')

label_relogio = Label(janela, text='00:00', font=('Times 150 bold'), fg='#DB524D', bg='#97CDB5')
label_relogio.place(x=50,y=50)

botao_play = Button(janela, text='Play', width=10, height=2, bg='#FF6242', fg='white', font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
botao_play.place(x=650, y=270)
botao_pause = Button(janela, text='Pause', width=10, height=2, bg='#FF6242', fg='white', font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
botao_pause.place(x=770, y=270)

janela.mainloop()

