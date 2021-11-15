'''Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.'''

from lista import Lista

lista_personajes = Lista()
personajes = [
    {'name':'Iron man','Anio': 1958, 'Casa' : 'Marvel', 'Biografia' : 'Traje'},
    {'name':'Wolverine','Anio': 1950, 'Casa' : 'Marvel', 'Biografia' : 'Traje'},
    {'name':'Hulk','Anio': 2002, 'Casa' : 'Marvel', 'Biografia' : 'Es verde'},
    {'name':'Linterna verde','Anio': 2003, 'Casa' : 'DC', 'Biografia' : 'Armadura'},
    {'name':'Dr Strange','Anio': 2004, 'Casa' : 'DC', 'Biografia' : 'Armadura'},
    {'name':'Star Lord','Anio': 2005, 'Casa' : 'DC', 'Biografia' : 'Armadura'},
    {'name':'Mujer Maravilla','Anio': 2006, 'Casa' : 'DC', 'Biografia' : 'traje'},
    {'name':'Capitana Marvel','Anio': 555, 'Casa' : 'Marvel', 'Biografia' : 'ropita'},
    {'name':'Blade','Anio': 2007, 'Casa' : 'Marvel', 'Biografia' : 'Traje'},
    {'name':'Flash','Anio': 2005, 'Casa' : 'Marvel', 'Biografia' : 'Armadura'},
]


for elementos in personajes:
    lista_personajes.insertar(elementos,'name')


print('----------------------------')
#A
lista_personajes.eliminar('Linterna verde','name')
print('----------------------------')
#B
poswolverine= lista_personajes.busqueda('Wolverine','name')
print('el anio de wolverine es :',lista_personajes.obtener_elemento(poswolverine)['Anio'])
print('----------------------------')
#C
posDr= lista_personajes.busqueda('Dr Strange','name')
lista_personajes.obtener_elemento(posDr)['Casa']= 'Marvel'
print('----------------------------')
#D
for i in range(0,lista_personajes.tamanio()):
    if lista_personajes.obtener_elemento(i)['Biografia'].find('Traje')!= -1 or lista_personajes.obtener_elemento(i)['Biografia'].find('Armadura')!= -1:
        print(lista_personajes.obtener_elemento(i)['name'])
print('----------------------------')
#E
for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if x['Anio'] < 1963:
        print('menores a 1963: ',x['name'],x['Casa'])
print('----------------------------')

#F
poscapitana= lista_personajes.busqueda('Capitana Marvel','name')
print('Casa de capitana marvel :',lista_personajes.obtener_elemento(poscapitana)['Casa'])
print('----------------------------')

posmaravilla= lista_personajes.busqueda('Mujer Maravilla','name')
print('Casa de Mujer Maravilla :',lista_personajes.obtener_elemento(posmaravilla)['Casa'])
print('----------------------------')

#G
pos_infoFlash= lista_personajes.busqueda('Flash','name')
print('Datos de Flash :',lista_personajes.obtener_elemento(pos_infoFlash))

print('----------------------------')
pos_infoStar= lista_personajes.busqueda('Star Lord','name')
print('Datos de Star Lord :',lista_personajes.obtener_elemento(pos_infoStar))

print('----------------------------')
#punto H
for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if (x['name'][0]=="B"):
        print('Los nombres que empiezan con la letra B son: ',x['name'])

for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if (x['name'][0]=="M"):
        print('Los nombres que empiezan con la letra M son: ',x['name'])

for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if (x['name'][0]=="S"):
        print('Los nombres que empiezan con la letra S son: ',x['name'])

print('----------------------------')
#Punto I
contador_casamarvel=0
contador_casadc=0
for i in range(0,lista_personajes.tamanio()):
    x = lista_personajes.obtener_elemento(i)
    if x['Casa'] == "Marvel":
        contador_casamarvel=contador_casamarvel+1
    else:
        contador_casadc=contador_casadc+1

print('La cantidad de superheores de la casa marvel son: ',contador_casamarvel)
print('La cantidad de superheores de la casa dc son: ',contador_casadc)

print('----------------------------')

lista_personajes.barrido()
