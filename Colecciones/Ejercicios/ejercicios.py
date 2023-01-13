'''
    ESCRIBA UN PRGRAMA QUE TENGA UNA LISTA,
    ELIMINE LOS ELEMENTOS REPETIDOS
    MOSTRAR LA NUEVA LISTA
'''

# lista = ['a', 'b', 'c', 'a', 'a', 'd', 'e', 'f', 'g', 'h', 'c', 'b']

'''
    Primera opción
conjunto = set(lista)
lista = list(conjunto)
lista.sort()
'''

''' Segunda opción
lista2 = list(set(lista))
lista2.sort()
print(lista2)

'''

################################################################################


'''' Escriba un programa que tenga dos listas y que se creen las siguienteslistas:

Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.


'''


# lista = [1,2,3,4,4,5,5,1,1,2,6,7,8,9,10,7,8]
# lista2 = [1,2,3,4,7,8,9,10,11,11,1,2,3,12,13]

# a = set(lista)
# b = set(lista2)

# union = list(a | b)
# lista_de_A = list(a - b)
# lista_de_B = list(b - a)
# insterseccion = list( a & b )


# print(f'Lista de palabras que aparecen en las dos listas: {union}')
# print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {lista_de_A}')
# print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera: {lista_de_B}')
# print(f'Lista de palabras que aparecen en ambas listas.: {insterseccion}')

''' Escriba un programa donde cree una lista con los siguientes personajes
    del señor de los anillos

    Nombre: Aragon                Nombre: Gandalf           Nombre: Legolas
    Clase: Guerrror               Clase: Mago               Clase: Arquero
    Raza: Dúnadan del Norte       Raza: Istar               Raza: Elfo Sindar
'''

personajes_serie = []

Aragon = {'Nombre':'Aragon', 'Clase':'Guerrero', 'Raza':'Dúnadan del Norte'}
personajes_serie.append(Aragon)

Gandalf = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Istar'}
personajes_serie.append(Gandalf)

Legolas = {'Nombre':'Aragon', 'Clase':'Arquero', 'Raza':'Elfo Sindar'}
personajes_serie.append(Legolas)

print(personajes_serie)

