#Se tiene una circunferencia de radio r, inscrita en un triángulo de lados a,b,c. Encuentre el área de este triángulo en función de a,b,c y r


a: float
b: float
c: float
r: float
area: float

# entrada
a=float(input("Ingrese lado a: "))
b=float(input("Ingrese lado b: "))
c=float(input("Ingrese lado c: "))
r=float(input("Ingrese radio: "))

# proceso
area=(a+b+c)*r/2

# salida
print(f'El área del triángulo es: {area}')
