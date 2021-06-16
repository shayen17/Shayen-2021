from lista import Lista

lista_pers = Lista()
personajes = [
    {'Nombre':'Iron man','Anio_ap':2000,'Superheroe':True},
    {'Nombre':'Wolverine','Anio_ap':2200,'Superheroe':True},
    {'Nombre':'Scalet Witch','Anio_ap':2003,'Villano':False},
    {'Nombre':'Star Lord','Anio_ap':2040,'Villano':False},
    {'Nombre':'Thor','Anio_ap':2030,'Superheroe':True},
    {'Nombre':'Capitana Marvel','Anio_ap':2300,'Superheroe':True},
    {'Nombre':'Blade','Anio_ap':2070,'Superheroe':True},
]

lista_aux = Lista()
Personajes_aux= [
    {'Nombre':'Black Widow','Anio_ap':2080,'Superheroe':True},
    {'Nombre':'Hulk','Anio_ap':20090,'Villano':False},
    {'Nombre':'Rocket Racoonn','Anio_ap':20004,'Superheroe':True},
    {'Nombre':'Loki','Anio_ap':20030,'Villano':False},
]

for elementos in personajes:
    lista_pers.insertar(elementos,'Nombre')

Lista2 = Lista()
for elementos in personajes:
    Lista2.insertar(elementos,'Anio_ap')

#A
for i in range(0,lista_pers.tamanio()):
    posThor= lista_pers.busqueda('Thor','Nombre')
    x = lista_pers.obtener_elemento(i)
    if (x['Nombre']=="Thor"):
        print('La posicion de Thor es :',posThor)


#B
posScarlet= lista_pers.busqueda('Scalet Witch','Nombre')
lista_pers.obtener_elemento(posScarlet)['Nombre']= 'Scarlet Witch'

#C
for elementos in Personajes_aux:
    lista_aux.insertar(elementos,'Nombre')

for i in range(0,lista_aux.tamanio()):
    lista_pers.insertar(lista_aux.obtener_elemento(i),'Nombre')


#D
for i in reversed(range(lista_pers.tamanio())):
    print(lista_pers.obtener_elemento(i))

#E
print('Personaje posicion 7 :',lista_pers.obtener_elemento(7)['Nombre'])

#F
for i in range(0,lista_pers.tamanio()):
    x = lista_pers.obtener_elemento(i)
    if (x['Nombre'][0]=="C"):
        print('Los nombres que empiezan con la letra C son: ',x['Nombre'])

for i in range(0,lista_pers.tamanio()):
    x = lista_pers.obtener_elemento(i)
    if (x['Nombre'][0]=="S"):
        print('Los nombres que empiezan con la letra S son: ',x['Nombre'])


#G
Lista2.barrido() #barrido año


lista_pers.barrido()