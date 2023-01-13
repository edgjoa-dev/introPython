#Diccionarios
#Los diccionarios aceptan enteros, cadenas, tuplas, listas dentro de ellos

diccionario = {'verde':'green', 'azul':'blue', 'grey':'gris', 'rojo':'green'} #para que sea un conjunto vacio se antepone la palabra set{}
#diccionario2 = {'Edgar':[11.02, 31], 'Joaquin':{'edad': 31, 'estatura':1.60}, 'rojo':'green'}
diccionario3 = {1:'CR7', 2:'Pelé', 3:'Messi', 4:'Maradonna', 5:'Modric'}

    #Seleccionar un elmento del diccionario
#print(diccionario['azul'])


    # agregar un elemento en el diccionario
#diccionario['amarillo'] = 'yellow' #Los diccionarios no se ordenan de acuerdo alos datos de entrada son desordenados

    # modificar un elemento en el diccionario
#diccionario['azul'] = 'BLUE'


    # eliminar un elemento en el diccionario
#del(diccionario['azul'])

    # validar si un elemento deseado esta dentro del diccionario
#print(3 in diccionario)

    #Mostrar solo las claves del diccionario
print(diccionario3.keys())
print(diccionario3.values())
print(diccionario3.items()) #usualmente se usa con el bucle for
print(len(diccionario3))

    # Limpiar diccionario
diccionario3.clear()

#print(diccionario)