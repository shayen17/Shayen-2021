
#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
#colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
#actividades enumeradas a continuación:
#a. listado ordenado por nombre y por especie;
#b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
#c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#d. mostrar los Jedi de especie humana y twi'lek;
#e. listar todos los Jedi que comienzan con A;
#f. mostrar los Jedi que usaron sable de luz de más de un color;
#g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from lista import Lista
jedis = Lista()
jedis_especies = Lista()
pada_Yoda = []
pada_Luke = []
jediHumano = []
jeditwi_lek = []
jedis_con_A = []
sable_mas_de_un_color = []
sable_amarillo_o_violeta = []
padawans_de_Jin_y_Windu = []

file = open("jedis.txt")

lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1]
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5]
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if(len(jedi) > 8):
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] = jedi[9]
    jedis.insertar(jedi_data, 'name')
    jedis_especies.insertar(jedi_data,"species")
file.close()

#punto a
print("Listado por Nombre")
for i in range(jedis.tamanio()):
    jedi = jedis.obtener_elemento(i)
    if jedi["name"][0]  == "A" in jedi["name"]:
        jedis_con_A.append(jedi)

    if "luke skywalker" in jedi["master"]:
        pada_Luke.append(jedi["name"])
    elif "yoda" in jedi["master"]:
        pada_Yoda.append(jedi["name"])
    
    if "Qui-Gon Jin" in jedi["master"] or "Mace Windu" in jedi["master"]:
        padawans_de_Jin_y_Windu.append(jedi["name"])

    if "human" in jedi["species"]:
        jediHumano.append(jedi["name"])
    elif jedi["species"] == "twi'lek":
        jeditwi_lek.append(jedi["name"]) 

    if len(jedi["lightsaber_color"])>1:
        sable_mas_de_un_color.append(jedi["name"])  

    if "yellow" in jedi["lightsaber_color"] or "purple" in jedi["lightsaber_color"]:
        sable_amarillo_o_violeta.append(jedi["name"])
    print(jedi["name"])

print("Listado por Especie")
for i in range(jedis_especies.tamanio()):
    jedisSpe = jedis_especies.obtener_elemento(i)
    print(jedisSpe["species"])

#punto b
print("Ahsoka Tano")
posAhsokaTano = jedis.busqueda("Ahsoka Tano","name")
if posAhsokaTano>-1:
    print(jedis.obtener_elemento(posAhsokaTano))
print(">>Kit Fisto")
posKitFisto = jedis.busqueda("Kit Fisto","name")
if posKitFisto>-1:
    print(jedis.obtener_elemento(posKitFisto))

#punto c
print("Padawan de luke son")
for p in pada_Luke:
    print(p)

print("Padawan de yoda son")
for p in pada_Yoda:
    print(p)

#punto d
print("Jedis humanos")
for j in jediHumano:
    print(j)
print("Jedis Twi'lek")
for j in jeditwi_lek:
    print(j)

#punto e
print("jedis que comienzan en A")
for p in jedis_con_A:
    print(p["name"])

#punto f
print("Jedis que usaron un sable con mas de un color:")
for p in sable_mas_de_un_color:
    print(p)

#punto g
print("Jedis que usaron un sable amarillo o violeta:")
for i in sable_amarillo_o_violeta:
    print(i)

#punto h
print("Los padawans de Qui-Gon Jin y Mace Windu :")
if len(padawans_de_Jin_y_Windu = []
)==0:
    print("No tuvieron padawans")
else:
    for i in padawans_de_Jin_y_Windu:
        print(i)