from cola import Cola

# Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
# nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
# ni métodos de ordenamiento.

cola_valores1=Cola()
cola_valores2=Cola()
cola_combinada=Cola()


cola_valores11=[1,2,3,4,5]
cola_valores22=[6,7,8,9]


#carga
for elementos in cola_valores11:
    cola_valores1.arribo(elementos)

for elementos in cola_valores22:
    cola_valores2.arribo(elementos)

#---------------------------------------------------------------------------------
while (not cola_valores1.cola_vacia() and not cola_valores2.cola_vacia()):
    if cola_valores1.en_frente() <= cola_valores2.en_frente():
       cola_combinada.arribo(cola_valores1.atencion())
    else:
        cola_combinada.arribo(cola_valores2.atencion())

while not cola_valores1.cola_vacia():
    cola_combinada.arribo(cola_valores1.atencion())

while not cola_valores2.cola_vacia():
    cola_combinada.arribo(cola_valores2.atencion())
#-----------------------------------------------------------------------------------

#barrido
while not cola_combinada.cola_vacia():
    print(cola_combinada.atencion())


       










