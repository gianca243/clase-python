try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("ocurrio un error")
else:
    print("no paso ningun error")
finally:
    print("se ejecuta siempre")
