#Calcule la suma de los cuadrados de los primeros números naturales.

n: int
s: int

# entrada
n = int(input("Ingrese el número de términos: "))

# proceso
s=n*(n+1)*(2*n+1)/6

# salida
print(f'La suma de los cuadrados de los {n} primeros términos es: {s}')
