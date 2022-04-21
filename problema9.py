#Calcule el área total de un cilindro recto de radio y altura conocida.


r: float
h: float
AreaTotalcil: float

# Entrada
r=float(input("Ingrese radio del cilindro: "))
h=float(input("Ingrese altura del cilindro: "))

# proceso
AreaTotalcil=6.28*r*(r+h)

#salida
print(f"Area pedida: {AreaTotalcil} ")
