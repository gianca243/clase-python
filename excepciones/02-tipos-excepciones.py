try:
    n1 = int(input("Ingresa primer numero: "))
except ValueError as e:
    print(type(e))
    print("inserta un valor coherente con int")
except NameError as e:
    print("omg")
