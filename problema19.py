#Convierta el ángulo sexagesimal UºV'W'' a grados, minutos y segundos centesimales.

U: float
V: float
W: float
S: float
C: float
gra: float
min: float
seg: float

# entrada
U = float(input("Ingrese U: "))
V = float(input("Ingrese V: "))
W = float(input("Ingrese W: "))


# proceso
S = U + V/60 + W/3600
C = 10*S/9
gra = int(C)
min = int((C-gra)*100)
seg = ((C-gra)*100-min)*100

print("El ánguylo equivale a centesimal a: ")
print(gra, "gra ", min, "min", seg , "seg" )


