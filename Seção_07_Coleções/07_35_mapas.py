"""
Mapas

receitas = {}.fromkeys(["jan", "fev", "mar", "abr", "mai"], 250)
print(receitas)
print(receitas.keys())
print(receitas.values())
print(receitas.items())

for chave in receitas.keys():
    print(chave)

for valor in receitas.values():
    print(valor)

# ou

print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas))

for chave, valor in receitas.items():
    print(f"Em {chave} a receita foi de {valor}.")

"""

