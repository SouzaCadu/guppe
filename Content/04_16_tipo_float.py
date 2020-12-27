"""
Tipo  float

Tipo real, decimal

Casas decimais

Obs
"""

# Errado do ponto de vista do float, gera uma tupla
valor = 1, 44
print(valor, type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor, type(valor))

# Dupla atribuição
v1, v2 = 1, 44
print(v1, type(v1))
print(v2, type(v2))

# Conversão de float em int
"""
Há perda de precisão
"""

res = int(valor)
print(res, type(res))

# números complexos
var1 = 5j
print(var1, type(var1))

# Informação sobre as operações aceitas
print(dir(valor))
