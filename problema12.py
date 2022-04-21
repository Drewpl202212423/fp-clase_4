#En un triangulo rectángulo, calcule la longitud de la hipotenusa conociendo las longitudes de sus catetos.

from math import sqrt

# entrada
a = int(input("Ingrese lado a: "))
b = int(input("Ingrese lado b: "))

# proceso
c = sqrt(a*a + b*b)
# salida
print(f'la longitud de la hipotenusa es: {c}')
