from lista import Lista

ListaEntrenadores = Lista()


Entrenadores = [
    { 'nombre' : 'ash','torneos ganados' : 1,'B-perdidas' : 5,'B-ganadas' : 8 ,'pokemones' : Lista()},
    { 'nombre' : 'misty','torneos ganados' : 4,'B-perdidas' : 3,'B-ganadas' : 7 ,'pokemones' : Lista()},
    { 'nombre' : 'rojo','torneos ganados' : 8,'B-perdidas' : 0,'B-ganadas' : 10 ,'pokemones' : Lista()}
]


pokemon1 = {'nombre' : 'pikachu','nivel': 16,'tipo' : 'electrico', 'subtipo' : 'luchador'}
pokemon2 = {'nombre' : 'charmander','nivel': 15,'tipo' : 'fuego', 'subtipo' : ''}
pokemon3 = {'nombre' : 'squartul','nivel': 18,'tipo' : 'agua', 'subtipo' : ''}
pokemon4 = {'nombre' : 'sindaquil','nivel': 20,'tipo' : 'fuego', 'subtipo' : ''}
pokemon5 = {'nombre' : 'hitmonlee','nivel': 33,'tipo' : 'luchador', 'subtipo' : 'roca'}
pokemon6 = {'nombre' : 'wingull','nivel': 16,'tipo' : 'agua', 'subtipo' : 'volador'}
pokemon7 = {'nombre' : 'tyrantrum','nivel': 160,'tipo' : 'roca', 'subtipo' : 'dragon'}




for entrenador in Entrenadores:
    ListaEntrenadores.insertar(entrenador , 'nombre')

pos = ListaEntrenadores.busqueda('ash', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon1, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon4, 'nombre')
    

pos = ListaEntrenadores.busqueda('misty', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon3, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon6, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon3, 'nombre')

pos = ListaEntrenadores.busqueda('rojo', 'nombre')
if pos != -1:
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon3, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon2, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon5, 'nombre')
    ListaEntrenadores.obtener_elemento(pos)['pokemones'].insertar(pokemon7, 'nombre')


# a

print('ingrese el entrenador')
entrena = input()
if entrena == 'ash':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('ash','nombre'))['pokemones'].tamanio())
elif entrena == 'misty':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('misty','nombre'))['pokemones'].tamanio())
elif entrena == 'rojo':
    print(ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('rojo','nombre'))['pokemones'].tamanio())
else:
    print('el nombre no existe')

print()
# b

pos_max = -1

for i in range(ListaEntrenadores.tamanio()):
    ganador = ListaEntrenadores.obtener_elemento(i)
    if ganador['torneos ganados'] >= 3 :
        pos_max = i
        print(ganador['nombre'])

print()
# c       

nivel_max = 0
pos_nivel_max = -1
entrenador_max = ListaEntrenadores.obtener_elemento(pos_max)


for i in range(entrenador_max['pokemones'].tamanio()):
    if(entrenador_max['pokemones'].obtener_elemento(i)['nivel'] > nivel_max):
        nivel_max = entrenador_max['pokemones'].obtener_elemento(i)['nivel']
        pos_nivel_max = i

print(entrenador_max['nombre'] ,': ' ,entrenador_max['pokemones'].obtener_elemento(pos_nivel_max)['nombre'])

print()
# d

print(entrenador_max['nombre'], entrenador_max['torneos ganados'], entrenador_max['B-ganadas'], entrenador_max['B-perdidas'])
print('pokemones: ')
entrenador_max['pokemones'].barrido()

print()
# e

pos_max = -1

for i in range(ListaEntrenadores.tamanio()):
    batallas = ListaEntrenadores.obtener_elemento(i)
    porcentaje_victoria = (batallas['B-ganadas'] * 100) /(batallas['B-ganadas']+ batallas['B-perdidas'])
    if porcentaje_victoria > 79 :
        pos_max = i
        print(batallas['nombre'])

print()
# f

for i in range(ListaEntrenadores.tamanio()):
    entrena = ListaEntrenadores.obtener_elemento(i)
    for n in range(entrena['pokemones'].tamanio()):
        if entrena['pokemones'].obtener_elemento(n)['tipo'] == 'agua' and entrena['pokemones'].obtener_elemento(n)['subtipo'] == 'volador':
            print('Tipo agua/volador: ',entrena['pokemones'].obtener_elemento(n)['nombre'])


print()
# g

acumulador = 0
pos_pokemon = ListaEntrenadores.busqueda('ash','nombre')
entrena_pokemon = ListaEntrenadores.obtener_elemento(pos_pokemon)
for i in range(entrena_pokemon['pokemones'].tamanio()):
    acumulador += entrena_pokemon['pokemones'].obtener_elemento(i)['nivel']

promedio = acumulador / entrena_pokemon['pokemones'].tamanio()

print('promedio de nivel de los pokemones: ',promedio)


print()
# h


for i in range(ListaEntrenadores.tamanio()):
    tiene_pokemon = ListaEntrenadores.obtener_elemento(i)
    for n in range(tiene_pokemon['pokemones'].tamanio()):
        if tiene_pokemon['pokemones'].obtener_elemento(n) == pokemon3:
            print(tiene_pokemon['nombre'],'tiene el pokemon: ',pokemon3['nombre']) 

print()
# i


for i in range(ListaEntrenadores.tamanio()):
    entrena_p = ListaEntrenadores.obtener_elemento(i)
    for n in range(entrena_p['pokemones'].tamanio()):
        contador_repetido = 0
        for j in range(entrena_p['pokemones'].tamanio()):
            if entrena_p['pokemones'].obtener_elemento(n)['nombre'] == entrena_p['pokemones'].obtener_elemento(j)['nombre']:
                contador_repetido += 1
                if contador_repetido > 1:
                    break
        if contador_repetido > 1:
            print('el entrenador: ',entrena_p['nombre'], 'tiene pokemones repetidos')
            break 

print()
# j

for i in range(ListaEntrenadores.tamanio()):
    entrena_bus = ListaEntrenadores.obtener_elemento(i)
    for n in range(entrena_bus['pokemones'].tamanio()):
        if entrena_bus['pokemones'].obtener_elemento(n) == pokemon6 or entrena_bus['pokemones'].obtener_elemento(n) == pokemon7:
            print(entrena_bus['nombre'])
        
                        
print()
# k.

print('ingrese el entrenador')
entrena = input()
if entrena == 'ash':
    entre = ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('ash','nombre'))
    print ('ingrese el nombre del pokemon')
    pokemon = input()
    for n in range(entre['pokemones'].tamanio()):
        if entre['pokemones'].obtener_elemento(n)['nombre'] == pokemon:
            print(entre,entre['pokemones'].obtener_elemento(n))
        
    

elif entrena == 'misty':
    entre = ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('misty','nombre'))
    print ('ingrese el nombre del pokemon')
    pokemon = input()
    for n in range(entre['pokemones'].tamanio()):
        if entre['pokemones'].obtener_elemento(n)['nombre'] == pokemon:
            print(entre,entre['pokemones'].obtener_elemento(n))
        

elif entrena == 'rojo':
    entre = ListaEntrenadores.obtener_elemento(ListaEntrenadores.busqueda('rojo','nombre'))
    print ('ingrese el nombre del pokemon')
    pokemon = input()
    for n in range(entre['pokemones'].tamanio()):
        if entre['pokemones'].obtener_elemento(n)['nombre'] == pokemon:
            print(entre,entre['pokemones'].obtener_elemento(n))

            

else:
    print('el nombre del entrenador no se encuentra')