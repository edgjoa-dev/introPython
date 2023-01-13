#Listas

lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo', 15, 20.5, True, [1,2,3], 1 ,1, 2, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7]
# lista1=[1,2,3]
# lista2=[4,5,6]
#print(lista)

    #mostrar 1 solo elemnto en especifico

#imprimir solo jueves
#print(lista[3])

    #Acceder a el sábado por detras de la lista

#print(lista[-2])

    #imprimir desde lunes a miercoles y desde el inicio hasta el viernes
# print(lista[0:3])
# print(lista[:5])

    #imprimir viernes sabado y domingo
# print(lista[4:8])
# print(lista[:8])

    #Determinar cuantos elementos tiene la lista
# print(len(lista))

    #agragar un elemto al final de la lista
#lista.append(4)

    #agragar un elemto en una pocición e especifico
#lista.insert(3,4)

    #agragar varios elementos al final de la lista
#lista.extend([5,6,7])

    #Sumar dos listas
# suma_listas = lista1 + lista2
# print(suma_listas)

    #Validar si un elemnto se encuentra dentro de la lista
# print('Miercoles' in lista)
# print(3 in lista)
# print(20.5 in lista)
# print(True in lista)

    #retornar el indice en el que se encuentra un elemento dentro de la lista
# print( lista.index('Lunes') )
# print( lista.index(20.5) )
# print( lista.index(True) )
# print( lista.index([1,2,3]) )

    #Validar cuentas veces se encuentra un elemento dentro de la lista
# print(lista.count('Lunes'))
# print(lista.count(20.5))
# print(lista.count(1))

    #Eliminar elementos de la lista
#lista.pop()
#lista.pop(3)
#lista.remove(7)
#lista.remove('Lunes')
#lista.clear()

    #Dar vuelta a la lista
#lista.reverse()

    #Ordenar la lista
#lista.sort()
#lista.sort(reverse=True)



print(lista)