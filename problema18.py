#Existen muchas maneras de medir ángulos. El Sistema sexagesimal divide una circunferencia en 360 partes llamándola a cada una "grado sexagesimal", cada grado sexagesimal está dividido en 60 mimutos y cada minuto en 60 segundos, (por ejemplo 20º15'21'') El Sistema Centesimal considera como unidad de medida "el grado centesimal" y equivle a 400 ava. parte de la circunferencia, cada grado sentesimal está dividido en 100 minutos centesimales y cada minuto en 100 segundos centesimales (por ejemplo: 20g15m21s). Sl sistema Radial utiliza como unidad de medida un arco cuya longitud es igual a su radio, como la longitud de la circunferencia es l=2 * pi * r, y como en trigonometría se considera un círculo base con radio r=l, entonces toda la circunferencia tendrá 2 * pi * radianes.

S: float
C: float
R: float
pi: float

pi = 3.14


S = float(input("Ingrese el grado sexagesimal: "))

C = (10/9)*S
R = (pi / 180)*S

print(f'{S} grados Sexagesimal es {C} grados centecimales y {R} grados radianes')

print(S," grados sexagesimales")
print("es", C , " grados centesimales")
print("es", R , " grados radianes")
