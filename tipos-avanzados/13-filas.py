from collections import deque
lista = [2, 3, 4]

fila = deque([1, 2])
# fila.append(3)
# fila.append(4)
# fila.append(5)
print(fila)
fila.popleft()
fila.popleft()
print(fila)
if not fila:
    print("fila vacia")
