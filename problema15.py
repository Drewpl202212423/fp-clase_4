#Convierta el complejo c = a + b * i, a sus coordenadas polares.

from math import sqrt, atan
a: float
b: float
w: float
p: float

# entrada
a = int(input("Ingrese la parte real: "))
b = int(input("Ingrese la parte imaginaria: "))
# proceso
p=sqrt(a*a + b*b)
w=atan(a/b)
# salida
print(f'ángulo: {w}')
print(f'distancia: {p}')
