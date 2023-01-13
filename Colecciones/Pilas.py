#Pilas
    #En las pilas el primer elemento enentrar es el ultimo en salir
    #Al agregar elemtos se agregan al final de la pila
pila = [1,2,3,4]

    #AGREGAR ELEMTOS POR EL FINAL
pila.append(5)

    #SACAR ELEMTOS
subs = pila.pop()
print(f'El elemento sustraido de la pila es: {subs}')


print(pila)