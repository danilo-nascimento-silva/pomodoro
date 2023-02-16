import time

t = input("Digite o tempo (em segundos): ")
pomodoro = t
pausa_c = 5
pausa_l = 10
pausas = 0

if t.isdigit():
    t = int(t)
    pomodoro = int(t)
else:
    print("Entrada inválida!")
    quit()

while True: 
    minutes, seconds = divmod(t, 60)    
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

    if t == 0 and pausas == 4:
        print('Pausa Longa')
        pausas = 0  
        while pausa_l != 0:
            minutes, seconds = divmod(pausa_l, 60)    
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            pausa_l -= 1
        print('Acabou a pausa curta')
        t = pomodoro

    if t == 0:
        print('Pausa Curta')
        pausas += 1 
        while pausa_c != 0:
            minutes, seconds = divmod(pausa_c, 60)    
            timer = "{:02d}:{:02d}".format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            pausa_c -= 1
        print('Acabou a pausa curta')
        t = pomodoro


