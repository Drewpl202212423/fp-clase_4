#Calcule el área de un rombo de diagonales conocidas.

d1: float
d2: float
AreaRombo: float

#entrada
d1 = float(input("Ingrese diagonal mayor: "))
d2 = float(input("Ingrese diagonal maenor: "))

# proceso
AreaRombo=d1*d2/2

# salida
print(f'El área del rombo es: {AreaRombo}')
