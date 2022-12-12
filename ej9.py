import random

NumerosMazo=[1,2,3,4,5,6,7,8,9,10,11,12]
Palos = ["Oro", "Copas", "Espadas", "Bastos"]

def Ordenar(Valores):
    for i in range(len(Valores)):
        ElementoPequeno = i
        for j in range(i+1,len(Valores)):
            if Valores[j] < Valores[ElementoPequeno]:
                ElementoPequeno=j
        Valores[i],Valores[ElementoPequeno] = Valores[ElementoPequeno], Valores[i]
    return Valores

MazoOrdenado=[]
for i in Palos:
    for j in NumerosMazo:
        MazoOrdenado.append([i,j])

MazoAleatorio=[]
while True:
    if(len(MazoOrdenado)>0):
        IDCartaAleatorio = random.randint(0,len(MazoOrdenado)-1)
        MazoAleatorio.append(MazoOrdenado[IDCartaAleatorio])
        del MazoOrdenado[IDCartaAleatorio]
    else:
        break
print('\n1) Mazo aleatorio: \n {}'.format(MazoAleatorio))

PilasPalos={}
for i in Palos:
    PilasPalos[i]=[]

for i in MazoAleatorio:
    PilasPalos[i[0]].append(i[1])
print('\n2) Pilas generadas para cada palo de la bara aleatorio: \n ')
for i in PilasPalos:
    print('Palo {}: {}'.format(i,PilasPalos[i]))


print('\n 3) Seleccione la pila que quiere ordenar')
for i in PilasPalos:
    print('---> {}'.format(i))
PilaAOrdenar=input()

PilaOrdenada = Ordenar(PilasPalos[PilaAOrdenar])
print('\nPila del palo {} ordenada:\n{}'.format(PilaAOrdenar,PilaOrdenada))