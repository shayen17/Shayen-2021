from cola import Cola
from pila import Pila

Cola_not=Cola()
Cola_aux=Cola()
Pila_temp=Pila()


class Notificaciones(object):
    def _init_(self,horantf, app, msj):
        self.horantf = horantf
        self.app = app
        self.msj= msj


Cola_not.arribo(Notificaciones(06.06,"Facebook","Python"))
Cola_not.arribo(Notificaciones(15.30,"Twitter","???"))
Cola_not.arribo(Notificaciones(12.05,"Instagram",":D"))

if Cola_not.en_frente().app == 'facebook':
    Cola_not.atencion()
else: 
    Cola_aux.arribo(Cola.atencion)

if Cola_not.en_frente().app == 'Instagram':
    Pila_temp.apilar(Cola_not.en_frente())
    Cola_aux(Cola_not.atencion())


