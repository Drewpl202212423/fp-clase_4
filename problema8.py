#Calcule el volumen de un cilindro recto conociendo su radio y su altura.
r: float
h: float
V: float
pi: (3.14)

# entrada
r=float(input("Ingrese el radio del cilindro: "))
h=float(input("Ingrese altura del cilibdro: "))
pi=float(3.14)

# proceso
V= pi * (r * r) * h

# salida
print("El volumen del cilindro es:", V)
