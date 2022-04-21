#Para medir la temperatura existen 4 escalas, las cuales guardan la siguiente proporción.grafico.Si C, F, K y R son los valores de una misma temperatura en grados Celsius (Centígrados), Farenheit, Kelvin y Rankine respectivamente, deduzca las fórmulas para convertir una temperatura de una escala a otra. Luego lea una temperatura en grados Celsius y diga a cuantos grados equivale en Farenheit, Kelvin y Rankine.

# entrada
C = float(input("Ingrese la temperatura en grados celsius: "))
F = (9/5)*C + 32
K = C + 273
R = (9/5) * C + 492
print(f'{C} Grados celsius es {F} grados farenheit ')
print(f'{C} Grados celsius es {K} grados kelvin ')
print(f'{C} Grados celsius es {R} grados rankine ')
