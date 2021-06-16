#barrido recursivo
personajes = ['Luke', 'Yoda','Jar Binks']
def barrido_rec(lista,i):
    if i == (len(lista)):
        return(i)
    else:   
        return personajes(lista, i+1)

#barrido yoda

personajes = ['Luke', 'Yoda', 'Jar Binks']
def barrido_yoda(lista,i):
    if lista[i] == 'Yoda':
        return(i)
    else:   
        return personajes(lista, i+1)

print(barrido_rec())
print(barrido_yoda())