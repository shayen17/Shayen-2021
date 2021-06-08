from cola import Cola

cola_pers_plan = Cola()
cola_pers_aux = Cola()

class Personajes(object):
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

#cargamos 
cola_pers_plan.arribo(Personajes('Han Solo','Corelia'))
cola_pers_plan.arribo(Personajes('Luke Skywalker','Alderaan'))
cola_pers_plan.arribo(Personajes('Chewbacca','Tatooine'))
cola_pers_plan.arribo(Personajes('Han solo','Endor'))
cola_pers_plan.arribo(Personajes('Yoda','Tatooine'))
cola_pers_plan.arribo(Personajes('Jar Jar Binks','Endor'))


while (not cola_pers_plan.cola_vacia()):
    print(cola_pers_plan.en_frente().nombre)
    cola_pers_aux.arribo(cola_pers_plan.atencion())    
while (not cola_pers_aux.cola_vacia()):
    cola_pers_plan.arribo(cola_pers_aux.atencion())




while(not cola_pers_plan.cola_vacia()):
    aux = cola_pers_plan.en_frente()
    if (aux.planeta =='Alderaan'):
        print('el personaje '+ aux.nombre + ' es de Alderaan')
    elif(aux.planeta =='Tatooine'):
        print('el personaje '+ aux.nombre + ' es de Tatooine')
    if (aux.nombre == 'Yoda'):
        #cola_pers_plan.mover_final()
        cola_pers_aux.arribo(Personajes('anterior a yoda','Marte'))
    cola_pers_aux.arribo(cola_pers_plan.atencion())
    if (aux.nombre == 'Jar Jar Binks'):
        cola_pers_aux.arribo(Personajes('adkjfjsdf','Marte'))

while (not cola_pers_aux.cola_vacia()):
    print(cola_pers_aux.en_frente().nombre)
    cola_pers_plan.arribo(cola_pers_aux.atencion())        









