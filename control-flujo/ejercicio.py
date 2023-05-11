mensaje = """
Bienvenidos a la calculadora
Para salir escribe salir
las operaciones son suma, multi, resta y div
"""
print(mensaje)
num1 = int(input("Ingresa número: "))
while True:
    operacion = input("Ingresa operacion: ")
    if operacion.lower() == "salir":
        break
    num2 = int(input("ingresa siguiente numero: "))
    if operacion.lower() == "sumar":
        num1 += num2
    elif operacion.lower() == "restar":
        num1 -= num2
    elif operacion.lower() == "multi":
        num1 *= num2
    elif operacion.lower() == "div":
        num1 /= num2
    else:
        print("valor no valido")
    print(f"el resultado es {num1}")
