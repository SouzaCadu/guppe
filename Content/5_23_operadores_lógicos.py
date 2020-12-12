"""
Estruturas lógicas and, or, not, is

operadores unários - not

operadores binários - and, or, is (comparação)
"""

ativo = True
logado = True

if ativo and logado:
    print("Bem vindo usuário!")
else:
    print("Você precisa fazer o log in. Cheque sua conta.")

if not ativo:
    print("Você precisa fazer o log in. Cheque sua conta.")
else:
    print("Bem vindo usuário!")

print(ativo is False)