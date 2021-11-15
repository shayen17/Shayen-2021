
""" Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido """

from lista import Lista
from random import randint
primer_lista = Lista()
segunda_lista = Lista()
lista_concatenada = Lista()

for i in range(5):
    primer_lista.insertar(i) #cargamos las dos listas
    segunda_lista.insertar(randint(1,10))

print('lista uno')
primer_lista.barrido()
print()

print('lista dos')
segunda_lista.barrido()
print()

cont_repetidos = 0

for i in range(primer_lista.tamanio()): #puntoA
    numero = (segunda_lista).obtener_elemento(i)
    primer_lista.insertar(numero)


print('listas concatenadas')
primer_lista.barrido()
print()

for i in range(primer_lista.tamanio()):#puntob
    numero = (segunda_lista.obtener_elemento(i)) 
    lista_concatenada.insertar(numero)
    
print ('dos concatenadas en una')
lista_concatenada.barrido()
print()
                
for i in range(primer_lista.tamanio()):
	num=primer_lista.obtener_elemento(i)
	pos = segunda_lista.busqueda(num)
	if (pos != -1):
		cont_repetidos =+1

while(primer_lista.tamanio()>0):#puntoD
    numero = (primer_lista.obtener_elemento(0)) 
    print('numero eliminado: ',numero)
    aux=primer_lista.eliminar(numero)
    

print('los elementos repetidos son: ', cont_repetidos)
print('sin repetir')

primer_lista.barrido()    

