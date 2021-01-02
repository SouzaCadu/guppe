"""
Funções com parâmetro padrão

- funções onde a passagem de parâmetro seja opcional, ou seja, quando eu
  estabeleço um valor padrão para o parâmetro, se o usuário informar um valor
  como argumento será usado o valor do argumento passado pelo usuário
- ao usar valores padrão eles DEVEM estar no final da declaração da função, do contrário
  há um erro na execução
- permite mais flexibilidade na hora de criar uma função
- qualquer tipo de dado pode ser usado como parâmetro padrão
- quanto ao escopo das variáveis, será dada preferência as variáveis locais
  em detrimento das globais de mesmo nome
- as variáveis criadas dentro da função só serão acessadas dentro do escopo da
  função, as variáveis criadas fora do escopo da função não podem ser acessadas
  para realizar operações dentro da função
- funções podem ser declaradas dentro de outras funções

# exemplo


print("Geek University")
print()


def exponencial(base, potencia=2):
    return base ** potencia


print(exponencial(2, 3))
print(exponencial(2))
print(exponencial(5))
print(exponencial(5, 2))


def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek!"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor!"
    return f"Olá {nome}!"


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao("Lars Ulrich"))
print(mostra_informacao(nome="Paul Richardson"))


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def mat(a, b, func=soma):
    return func(a, b)


print(soma(3, 8))
print(subtracao(12, 19))
print(mat(20, 14, subtracao))


# exemplo de funções aninhadas, não usual


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())


"""
