#El área de un triángulo en función el semiperímetro, dada por Herón es: area = sqrt(p(p-a)(p-b)(p-c)), donde a, b y c son los lados del triángulo y p=(a+b+c)/2 el semiperímetro. Calcular el área del triángulo aplicando la fomurla. 

from math import sqrt
a: float
b: float
c: float
p: float
AreaTriang: float

# entrada
print("Ingrese los lados de un triángulo")
a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))

# proceso
p = (a+b+c)/2
AreaTriang = sqrt(p*(p-a)*(p-b)*(p-c))


# salida
print(f'El área del triángulo es: {AreaTriang}')
