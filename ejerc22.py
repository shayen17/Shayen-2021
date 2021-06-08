from cola import Cola

Cola_personajes=Cola()
Cola_aux=Cola()


class Personajes(object):
    def __init__(self, nombre_per, nombre_superheroe,genero):
        self.nombre_per = nombre_per
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

#carga
Cola_personajes.arribo(Personajes('Tony Stark','Ironman','M'))
Cola_personajes.arribo(Personajes('Steve Rogers','Capitán América','M'))
Cola_personajes.arribo(Personajes('Natasha Romanoff','Black Widow','F'))
Cola_personajes.arribo(Personajes('Robert Bruce Banner','Hulk','M'))
Cola_personajes.arribo(Personajes('Carol Danvers','Capitana marvel','F'))
Cola_personajes.arribo(Personajes('Scott Lang','Hombre hormiga','M'))

# while (Cola_personajes.cola_vacia()):
#     print(Cola_personajes.en_frente().nombre_per)
#     Cola_personajes.arribo(Cola_personajes.atencion())   

#a
while(not Cola_personajes.cola_vacia()):
    aux = Cola_personajes.atencion()
    if (aux.nombre_superheroe =='Capitana marvel'):
        print('el nombre del personaje capitana marvel es:  '+ aux.nombre_per) 
    Cola_aux.arribo(aux)
#carga despues de que se vacia

while(not Cola_aux.cola_vacia()):
    Cola_personajes.arribo(Cola_aux.atencion())
# for elementos in Cola_personajes:
#      Cola_personajes.arribo(elementos)


while(not Cola_personajes.cola_vacia()):
    aux = Cola_personajes.atencion()
    if (aux.genero =='F'):
        print('Los personajes femeninos son: '+ aux.nombre_per) 
    Cola_aux.arribo(aux)

while(not Cola_aux.cola_vacia()):
    aux = Cola_aux.atencion()
    if (aux.genero =='M'):
        print('Los personajes masculinos son: '+ aux.nombre_per) 
    Cola_personajes.arribo(aux)       

while(not Cola_personajes.cola_vacia()):
    aux = Cola_personajes.atencion()
    if (aux.nombre_per =='Scott Lang'):
        print('el nombre del super heroe de Scott Lang es:  '+ aux.nombre_superheroe)
    Cola_aux.arribo(aux)
    # for elementos in Cola_personajes:
#      Cola_personajes.arribo(elementos)


while(not Cola_aux.cola_vacia()):
    aux = Cola_aux.atencion()
    if (aux.nombre_superheroe[0] == 'S' or aux.nombre_per[0]=='S'):
        print("Los personajes que su nombre empieza con la letra S son: " "Su nombre es: "+ aux.nombre_per +" Y su genero es: "+aux.genero) 
    Cola_personajes.arribo(aux)
# for elementos in Cola_personajes:
#      Cola_personajes.arribo(elementos)

while(not Cola_personajes.cola_vacia()):
    aux = Cola_personajes.atencion()
    if (aux.nombre_per =='Carol Danvers'):
        print('Carol pertenece a la cola y su nombre de super heroe es: '+aux.nombre_superheroe) 

# for elementos in Cola_personajes:
#      Cola_personajes.arribo(elementos)
