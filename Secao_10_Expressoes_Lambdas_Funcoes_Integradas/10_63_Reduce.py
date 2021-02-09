"""
Reduce

Precisa ser importada do módulo "functools". Deve ser usada apenas se necessário, pois
um loop for é preferível por ser mais inteligível. A função reduce recebe sempre dois parâmetros, a função
e o iterável.

Reduce funciona aplicando a função nos dois primeiros da coleção e guarda o resultado,
no passo seguinte aplica a função no resultado do passo 1, mais o terceiro dado da coleção,
assim, até o último elemento. Ou seja, a cada passo ela aplica a função passando
como primeiro elemento o resultado da aplicação anterior.

Exemplo:

from functools import reduce

dados = list(range(1, 12, 2))

res = reduce(lambda x, y: x * y, dados)

res1 = 1
for i in dados:
    res1 *= i

print(res, res1)

"""
