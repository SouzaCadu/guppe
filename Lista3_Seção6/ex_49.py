"""
Calcule o tempo que um ativo rendendo 2% ao mês será alcançado
por um rendimento com 1/3 do valor rendendo 5% ao mês.
"""

t = 1
ativo1 = (1 * 1.02 ** t)
ativo2 = ((1 / 3) * (1.05 ** t))

while ativo2 < ativo1:
    ativo1 += (1 * 1.02 ** t)
    ativo2 += ((1 / 3) * (1.05 ** t))
    t += 1
    if ativo1 == ativo2:
        break
print(f"O tempo necessário para igualar é de {t} mês.")