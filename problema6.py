#En un cuadrado cuyo lado es  a , se unen los puntos medios de sus 4 lados, formandose otro cuadrado cuyos puntos medios se unen también formando otro cuadrado, y así susesivamente. Calcule la suma de las áreas de todos los cuadrados asi formados.

a: float
s: float

#entrada
a = float(input("Ingrese lado del cuadrado inicial: "))

# proceso
s = 2*a*a

#salida
print(f'La suma d elas áreas es: {s}')
