#Conjuntos

a={1,2,3}
b={3,4,5}

#Verificar si el conjunto a es igual al conjunto b
# print( a == b)

################################################

#Realizar la union de los 2 conjuntos

# c = a|b
# print(c)

###############################################

#Intersección y la diferencia de 2 conjuntos

# interseccion = a & b
# dif = a - b

# print(f'el resultado de la intersección es: {interseccion}')
# print(f'el resultado de la diferencia de ambos conjuntos es: {dif}')

##############################################

#Diferencia simetrica entre 2 conjuntos

# c = a ^ b

# print(f'La diferencia simetrica entre los conjuntos son: {c}')

##############################################

    #Validar si un conjunto es subconjunto o Superconjunto o disconexos de otros 2
c={1,2,3,4,5}

print(b.issubset(c))
print(b.issuperset(c))
print(b.isdisjoint(c))
