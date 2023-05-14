pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo_elento = pila.pop()
print(ultimo_elento)
print(pila)
print(pila[-1])

if not pila:
    print("pila esta vacia")
