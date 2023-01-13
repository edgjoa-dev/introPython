#Tuplas

tupla = (4, 'Edgar', 6.8, [1,2,3], 4, 5, 5, 5,)

### Restricciones ###
# No se puede agragar lementos
# No se pueden modicar los valores de los elemntos dentr de la tupla
# No se puede eliminar un valor de la tupla

    #Si se pueden buscar y seleccionar

# print(tupla[1])
# print(tupla[-1])
# print(tupla[1:])
# print(tupla[:6])
# print(6.8 in tupla)
# print(tupla.index(5))
# print(tupla.count(5))
# print(len(tupla))

    #Convertir una tupla en lsita
lista = list(tupla) # La tupla original no se modifica al editar la lista con los nuevos valores
print(lista)
