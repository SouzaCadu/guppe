"""
funções com parâmetro de entrada

- são funções que recebem dados para serem processados dentro da função,
  esses parâmetros são obrigatórios.
- funções podem ter diversos parâmetros de entrada, separados por vírgula.
- o número de parâmetros deve ser obedecido pelo número de argumentos
  informados, ou seja, devem ser exatamente iguais.



# Exemplos


def quadrado(numero):
    return numero ** 2


print(quadrado(2))
print(quadrado(3))
print(quadrado(5))
print(quadrado(7))


def cantar_parabens(aniversariante):
    print("\nParabéns pra você!"
          "\nNessa data querida"
          "\nmuitas felicidades"
          "\nmuitos anos de vida!"
          f"\nViva a/o {aniversariante}!!!")


cantar_parabens("Ana")


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return(a + b) * msg


print(soma(2, 10))
print(multiplica(10, 9))
print(outra(5, 8, "  Geek  "))


# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f"Seu nome é {nome} {sobrenome}."


print(nome_completo("Bruce", "Wayne"))


# Argumentos nomeados (Keywords Arguments)
# Caso utilizemos o nome dos parâmetros nos argumentos para informá-los, podemos
# usar qualquer ordem

print(nome_completo(nome="Clarck", sobrenome="Kent"))
print(nome_completo(sobrenome="Xavier", nome="Charles"))


def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total += i
    return total  # return finaliza a função


print(soma_impares(range(15)))


"""
