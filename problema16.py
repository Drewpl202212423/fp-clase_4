#¿Cuál es el monto a devolver si nos prestan un capital c, a una tasa de interés t%, durante n periodos?

from math import pow
c: float
i: float
n: float
m: float

# entrada
c = float(input("Ingrese capital prestado: "))
t = float(input("Ingrese tasa de interes (en decimales): "))
n = float(input("Ingrse numero de periodos: "))

# proceso
m = c*pow(1+t,n)

# salida
print(f'El monto a devolver será: {m}')
