import numpy as np
import os
os.system('clear')
a=1
bus=np.zeros((10,4), dtype=object)
for i in range(10):
    for j in range(4):
        bus[i][j]= str(a)
        a=a+1
print(bus)
cont_asientos= 0
while cont_asientos == 0:
    asiento = input(" ¿Qué asiento desea comprar?\n")
    c=0
    for i in range(10):
        for j in range(4):
            if bus[i][j] == asiento:
                bus[i][j] = "X"
                print(bus)
                c = 1
    if c == 0:
        print("ASIENTO OCUPADO")             
    cont = input("desea seguir comprando?n\ 1.- SI 2. NO\n")
    if cont == 2:
        cont_asientos == 1
