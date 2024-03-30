# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)

ahora = datetime.now()

print(ahora)

# el segundo parametro recibe algo llamado directives indican como se crea el objeto de fecha
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

# python 3 strptime directives


print(fecha.strftime("%Y.%m.%d"))

print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)
