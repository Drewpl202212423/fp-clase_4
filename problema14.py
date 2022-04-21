#Calcule la distancia entre 2 puntos de coordenadas conocidas.

# librerias
from math import sqrt, pow
# entrada
x1 = int(input("ingrese abscisa del primer punto: "))
y1 = int(input("ingrese ordenada del primer punto: "))
x2 = int(input("ingrese abscisa del segundo punto: "))
y2 = int(input("ingrese ordenada del segundo punto: "))

# proceso
d = sqrt(pow(x2-x1,2)+pow(y2-y1,2))
# salida

print(f'La distancia entre los puntos es: {d}')
