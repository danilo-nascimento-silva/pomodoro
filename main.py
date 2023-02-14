import time

timer = float(input('Digite quantidade de tempo em minutos: '))
timer = int(timer*60)
print(timer)
p_curta = 10 #5*60
p_longa = 30 #15*60
pausas = 0

init_temp = time.time()

while True:
    contador = int(time.time() - init_temp)
    if timer == (contador):
        print('Pausa Curta')
        init_temp = time.time()
        while True:
            contador = int(time.time() - init_temp)
            if contador == p_curta:
                pausas += 1
                break
            else:
                print(contador)
                time.sleep(1)
    else:
        print(contador)
        time.sleep(1)