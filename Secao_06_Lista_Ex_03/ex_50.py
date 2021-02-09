"""
Calcule o tempo necessário para um objeto de 1.5 m que cresce 2 cm ao ano
ser alcançado por um objeto de 1.1 m que cresce 3 cm ao ano
"""

t = 1
obj1 = (1.5 + (0.02 * t))
obj2 = (1.1 + (0.03 * t))

while obj2 < obj1:
    obj1 = (1.5 + (0.02 * t))
    obj2 = (1.1 + (0.03 * t))
    t += 1
    if obj1 == obj2:
        break
print(f"O tempo necessário para igualar é de {t} anos.")